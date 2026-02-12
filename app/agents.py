import ast
from google.genai import types
from .model import get_client
from .config import MODEL_ID, TEMPERATURE
from .tools import read_file, write_file, parse_source_code, find_undocumented_nodes

class DocstringAgent:
    def __init__(self):
        self.client = get_client()

    def generate_docstring(self, node_type, name, code_segment):
        """Generates the actual docstring using Gemini."""
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
            response = self.client.models.generate_content(
                model=MODEL_ID,
                contents=prompt,
                config=types.GenerateContentConfig(temperature=TEMPERATURE)
            )
            return response.text.strip().strip('`')
        except Exception as e:
            print(f"GenAI Error for {name}: {e}")
            return None

    def process_file(self, file_path):
        """Main workflow for a single file."""
        source = read_file(file_path)
        if source is None: return

        tree = parse_source_code(source)
        if not tree: 
            print(f"Skipping (Empty/Invalid): {file_path}")
            return

        nodes = find_undocumented_nodes(tree)
        if not nodes:
            print(f"No changes needed: {file_path}")
            return

        print(f"Processing {file_path} ({len(nodes)} missing docstrings)...")
        
        lines = source.splitlines()
        modified = False

        for node in nodes:
            # Get the exact code for context
            code_segment = ast.get_source_segment(source, node)
            if not code_segment: continue

            docstring = self.generate_docstring(type(node).__name__, node.name, code_segment)
            
            if docstring:
                # Basic insertion logic
                insertion_line_idx = node.body[0].lineno - 1
                indentation = " " * node.col_offset + "    "
                formatted_doc = f"{indentation}{docstring}\n"
                lines.insert(insertion_line_idx, formatted_doc)
                modified = True
                print(f"  + Documented {node.name}")

        if modified:
            write_file(file_path, "\n".join(lines))