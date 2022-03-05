import os

def is_text_file(filepath, blocksize=512):
    """Check if a file is likely a text file (not binary)"""
    try:
        with open(filepath, 'rb') as f:
            block = f.read(blocksize)
        if b'\0' in block:
            return False
    except Exception as e:
        print(f"Skipping {filepath} (error: {e})")
        return False
    return True

def dump_directory(directory, output_file):
    with open(output_file, 'w', encoding='utf-8') as out:
        for root, dirs, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                if not is_text_file(filepath):
                    print(f"Skipping binary file: {filepath}")
                    continue
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
                    continue

                out.write(f"=== {filepath} ===\n")
                out.write(content)
                out.write("\n\n")  # Separate files by blank line

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python dump_files.py <directory> <output_file>")
    else:
        directory = sys.argv[1]
        output_file = sys.argv[2]
        dump_directory(directory, output_file)
        print(f"File dump complete. Output written to {output_file}")

