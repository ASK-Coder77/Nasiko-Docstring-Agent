import argparse
import os
from .agents import DocstringAgent

def main():
    parser = argparse.ArgumentParser(description="Epoch X Nasiko Docstring Agent")
    parser.add_argument("target", help="File or Folder to process")
    args = parser.parse_args()

    agent = DocstringAgent()
    target_path = args.target

    # [cite_start]Handle Recursive Folder structures [cite: 27]
    if os.path.isdir(target_path):
        for root, _, files in os.walk(target_path):
            for file in files:
                if file.endswith(".py"):
                    full_path = os.path.join(root, file)
                    agent.process_file(full_path)
    
    # Handle Single File
    elif os.path.isfile(target_path):
        agent.process_file(target_path)
    
    else:
        print("Invalid path provided.")

if __name__ == "__main__":
    main()