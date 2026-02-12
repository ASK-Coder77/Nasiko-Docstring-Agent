import ast
import time
from .tools import read_file, write_file, parse_source_code, find_undocumented_nodes

# Note: We don't even need to import the AI library here for Mock Mode
# This prevents ALL API-related crashes.

class DocstringAgent:
    def __init__(self):
        # We simulate a client connection
        pass

    def generate_docstring(self, node_type, name, code_segment):
        """
        MOCK GENERATION: Returns a template string immediately.
        This bypasses Google's API limits and errors completely.
        """
        print(f"  [MOCK] Generating professional docstring for {name}...")
        
        # This is the string that will appear in your Python files
        return f'''"""
    [AI Generated] Automatic documentation for {name}.
    
    This {node_type.lower()} was identified by the Nasiko Agent as missing a docstring.
    
    Args:
        TODO: Check specific arguments for {name}.
        
    Returns:
        None: (Placeholder return value)
    """'''

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
            # No wait time needed for Mock Mode!
            
            code_segment = ast.get_source_segment(source, node)
            if not code_segment: continue

            # Fix the _name_ error safely
            node_type = type(node).__name__

            docstring = self.generate_docstring(node_type, node.name, code_segment)
            
            if docstring:
                insertion_line_idx = node.body[0].lineno - 1
                indentation = " " * node.col_offset + "    "
                
                formatted_doc = f"{indentation}{docstring}\n"
                lines.insert(insertion_line_idx, formatted_doc)
                modified = True
                print(f"  + Success: Documented {node.name}")

        if modified:
            write_file(file_path, "\n".join(lines))
            print(f"Saved changes to {file_path}")