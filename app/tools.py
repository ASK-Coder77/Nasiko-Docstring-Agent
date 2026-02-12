import ast
import os

def read_file(file_path):
    """Reads a file and returns its content safely."""
    if not os.path.exists(file_path):
        return None
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def write_file(file_path, content):
    """Writes content back to the file."""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def parse_source_code(source):
    """Parses source code into an AST tree. Returns None if syntax is invalid."""
    if not source.strip():
        return None # Handle empty files
    try:
        return ast.parse(source)
    except SyntaxError:
        return None # Handle incomplete/invalid code

def find_undocumented_nodes(tree):
    """
    Traverses the AST and returns a list of FunctionDef and ClassDef nodes
    that are missing docstrings.
    """
    nodes = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
            if not ast.get_docstring(node):
                nodes.append(node)
    
    nodes.sort(key=lambda x: x.lineno, reverse=True)
    return nodes