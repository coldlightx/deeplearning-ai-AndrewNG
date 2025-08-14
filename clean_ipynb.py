import json
from glob import glob


def process_ipynb_file(file_path):

    print(f"Processing file: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        notebook = json.load(f)

    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            lines = cell["source"]
            new_lines = []
            i = 0
            while i < len(lines):
                if "### START CODE HERE ###" in lines[i]:
                    new_lines.append(lines[i])
                    new_lines.append("\n")
                    while i < len(lines) and "### END CODE HERE ###" not in lines[i]:
                        i += 1
                    if i < len(lines):
                        new_lines.append(lines[i])
                else:
                    new_lines.append(lines[i])
                i += 1
            cell["source"] = new_lines

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=2)
    print(f"Processed: {file_path}")


def main():
    ipynb_files = glob("**/*.ipynb", recursive=True)

    if not ipynb_files:
        print("No .ipynb files found in current directory!")
        return

    for file_path in ipynb_files:
        try:
            process_ipynb_file(file_path)
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")


if __name__ == "__main__":
    main()
