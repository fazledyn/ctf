import sys
import hashlib
from typing import List

def generate_hash(text: str) -> str:
    """Generate SHA256 hash for given text."""
    return hashlib.sha256(text.encode()).hexdigest()

def find_matching_string(target_hashes: List[str]) -> List[str]:
    """
    Find the original strings that generated the target hashes.
    Assumes each string is built by adding one character to the previous string.
    """
    base_string = ""
    found_strings = []
    
    # We know the pattern starts with "P" and builds up
    for i in range(len(target_hashes)):
        found = False
        # Try adding each printable ASCII character
        for char in range(32, 127):
            test_string = base_string + chr(char)
            test_hash = generate_hash(test_string)
            
            if test_hash == target_hashes[i]:
                found_strings.append(test_string)
                base_string = test_string
                found = True
                break
        
        if not found:
            print(f"Could not find match for hash {i + 1}")
            break
    
    return found_strings

def main():
    # Input your hashes here, one per line
    f = open(sys.argv[1])
    lines = f.readlines()

    target_hashes = []
    for line in lines:
        target_hashes.append(line.strip())

    print("\nSearching for matching strings...")
    found_strings = find_matching_string(target_hashes)
    
    print("\nResults:")
    for i, string in enumerate(found_strings):
        print(f"Hash {i + 1}: {string}")

if __name__ == "__main__":
    main()

