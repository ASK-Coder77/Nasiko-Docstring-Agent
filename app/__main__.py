import argparse
import os
from .agents import DocstringAgent

def main():
    parser = argparse.ArgumentParser()
    # Accept 'mode' (docstring) and 'target' (folder)
    parser.add_argument("mode", nargs="?", default="docstring", help="Mode: docstring")
    parser.add_argument("target", help="File or Folder")
    args = parser.parse_args()

    # Smart handling: If user forgets 'docstring' keyword, assume arg 1 is the folder
    target_path = args.target
    if args.mode not in ["docstring"]:
        target_path = args.mode 

    agent = DocstringAgent()
    
    if os.path.isdir(target_path):
        for root, _, files in os.walk(target_path):
            for file in files:
                if file.endswith(".py"):
                    agent.process_file(os.path.join(root, file))
    elif os.path.isfile(target_path):
        agent.process_file(target_path)
    else:
        print(f"Error: Path '{target_path}' not found.")

if __name__ == "__main__":
    main()