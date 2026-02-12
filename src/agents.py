import ast
import time
import ollama
from .config import MODEL_ID, TEMPERATURE
from .tools import read_file, write_file, parse_source_code, find_undocumented_nodes

class DocstringAgent:
    def __init__(self):
        print(f"✅ Agent initialized using Local AI: {MODEL_ID}")

    def generate_docstring(self, node_type, name, code_segment):
        """
        Generates a docstring using a local Ollama model.
        """
        prompt = f"""
        You are an expert Python developer. Generate a clean, concise **Google-style docstring** for the following {node_type}.
        
        Requirements:
        - Include 'Args:', 'Returns:', and 'Raises:' sections if applicable.
        - Do NOT wrap the output in markdown code blocks (```).
        - Return ONLY the raw docstring text (quoted in triple quotes).
        
        Code to document ({name}):
        {code_segment}
        """

        try:
            # Call the local Ollama API
            response = ollama.chat(model=MODEL_ID, messages=[
                {'role': 'user', 'content': prompt}
            ])
            
            # Extract the content from the response
            docstring = response['message']['content']
            
            # Clean up potential markdown formatting
            return docstring.strip().strip('`')
            
        except Exception as e:
            print(f"  !! Ollama Error for {name}: {e}")
            return None

    def process_file(self, file_path):
        source = read_file(file_path)
        if not source: return

        tree = parse_source_code(source)
        if not tree: return
        
        nodes = find_undocumented_nodes(tree)
        if not nodes: 
            print(f"No missing docstrings in: {file_path}")
            return

        print(f"Processing {file_path} ({len(nodes)} items)...")
        lines = source.splitlines()
        modified = False
        
        for i, node in enumerate(nodes):
            print(f"  Generating docstring for {node.name}...")
            
            code_segment = ast.get_source_segment(source, node)
            if not code_segment: continue

            node_type = type(node).__name__
            docstring = self.generate_docstring(node_type, node.name, code_segment)
            
            if docstring:
                insertion_line_idx = node.body[0].lineno - 1
                indentation = " " * node.col_offset + "    "
                
                # Ensure the docstring has correct indentation
                formatted_doc = f"{indentation}{docstring}\n"
                lines.insert(insertion_line_idx, formatted_doc)
                modified = True
                print(f"  + Success: Documented {node.name}")

        if modified:
            write_file(file_path, "\n".join(lines))
            print(f"Saved changes to {file_path}")