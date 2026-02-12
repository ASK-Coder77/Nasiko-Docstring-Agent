import ast
import os

def read_file(file_path):
    if not os.path.exists(file_path): return None
    try:
        with open(file_path, "r", encoding="utf-8") as f: return f.read()
    except: return None

def write_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as f: f.write(content)

def parse_source_code(source):
    if not source.strip(): return None
    try: return ast.parse(source)
    except: return None

def find_undocumented_nodes(tree):
    nodes = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
            if not ast.get_docstring(node): nodes.append(node)
    nodes.sort(key=lambda x: x.lineno, reverse=True)
    return nodes