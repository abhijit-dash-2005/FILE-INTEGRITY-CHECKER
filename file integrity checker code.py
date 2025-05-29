import hashlib
import os

def generate_file_hash(filepath):
    hasher = hashlib.sha256()
    try:
        print("Trying to open file:", filepath)  # Debug line
        with open(filepath, 'rb') as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        print("File not found:", filepath)
        return None

def save_hash(filepath, hash_value, db_path='hashes.txt'):
    with open(db_path, 'a') as f:
        f.write(f"{filepath}|{hash_value}\n")

def load_hashes(db_path='hashes.txt'):
    hash_dict = {}
    if os.path.exists(db_path):
        with open(db_path, 'r') as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) == 2:
                    hash_dict[parts[0]] = parts[1]
    return hash_dict

def check_file_integrity(filepath, db_path='hashes.txt'):
    current_hash = generate_file_hash(filepath)
    if current_hash is None:
        return

    stored_hashes = load_hashes(db_path)

    if filepath in stored_hashes:
        if stored_hashes[filepath] == current_hash:
            print(f"[OK] {filepath} is unchanged.")
        else:
            print(f"[WARNING] {filepath} has been modified!")
    else:
        print(f"[INFO] No stored hash found for {filepath}.")

def main():
    print("=== File Integrity Checker ===")
    print("1. Add file hash")
    print("2. Check file integrity")
    choice = input("Enter your choice (1/2): ")

    filepath = input("Enter file path: ").strip()

    if choice == '1':
        file_hash = generate_file_hash(filepath)
        if file_hash:
            save_hash(filepath, file_hash)
            print(f"Hash saved for {filepath}")
    elif choice == '2':
        check_file_integrity(filepath)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
