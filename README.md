# FILE-INTEGRITY-CHECKER
# COMPANY - CODTECH IT SOLUTIONS
# INTERN ID - CT04DL1017
# DOMAIN - CYBER SECURITY AND ETHICAL HACKING 
# DURATION - 4 WEEKS 
# MENTOR - NEELA SANTOSH KUMAR
# OUTPUT :- 
![Image](https://github.com/user-attachments/assets/da7918de-d067-4075-8088-0bca9627c889)

![Image](https://github.com/user-attachments/assets/31d2b431-f880-4c1f-bbcd-ff50e851b532)

# 🔐 File Integrity Checker in Python

This project is a simple yet effective **File Integrity Checker** written in Python. It uses the built-in `hashlib` library to generate cryptographic hashes (SHA-256) for files and compare them over time to detect unauthorized changes or tampering.

## 📌 Features

- ✅ Generate and save SHA-256 hash for any file.
- ✅ Verify the integrity of files by comparing current hash with the saved one.
- ✅ Lightweight, no external libraries required.
- ✅ Command-line interface for user input.
- ✅ Logs saved hashes in a `hashes.txt` file.

---

## 📁 Folder Structure

FILE INTEGRITY CHECKER/
├── file_integrity_checker.py
├── test.txt
└── hashes.txt # Created after first run

yaml
Copy
Edit

---

## ⚙️ How It Works

This tool works in two modes:

1. **Add File Hash**
   - Generates a SHA-256 hash of a given file.
   - Stores the hash with the filename in `hashes.txt`.

2. **Check File Integrity**
   - Regenerates the hash of the file.
   - Compares it with the saved one.
   - Displays whether the file is:
     - Unchanged ✅
     - Modified ⚠️
     - Not found in saved hashes ℹ️

---

## 🚀 How to Run

### Step 1: Prerequisites
- Python 3.x installed on your system.
- Any code editor (Visual Studio Code recommended).
- Basic terminal/command prompt knowledge.

### Step 2: Setup

1. Create a folder:
FILE INTEGRITY CHECKER

markdown
Copy
Edit

2. Add these files inside:
- `file_integrity_checker.py` — the main Python script.
- `test.txt` — any test file to check integrity.

3. Open the folder in **VS Code**.

### Step 3: Run the Program

#### Option A (Recommended):
1. Open terminal in VS Code.
2. Navigate to project folder:
```bash
cd "C:\path\to\FILE INTEGRITY CHECKER"
Run:

bash
Copy
Edit
python file_integrity_checker.py
Enter:

pgsql
Copy
Edit
1 (to add hash) or 2 (to check integrity)
File path:

Copy
Edit
test.txt
Option B (Using Full Path):
Run from any location but enter full file path when asked.

🧪 Example
mathematica
Copy
Edit
=== File Integrity Checker ===
1. Add file hash
2. Check file integrity
Enter your choice (1/2): 1
Enter file path: test.txt
Hash saved for test.txt
📝 How Hashes Are Stored
All hashes are saved in a file named hashes.txt in the format:

Copy
Edit
filename|hashvalue
Example:

Copy
Edit
test.txt|f2ca1bb6c7e907d06dafe4687e579fce9fc...
🧠 Use Cases
✅ Detecting changes in important system or config files.

✅ Ensuring file authenticity.

✅ Simple cybersecurity exercises or projects.

🛡️ Limitations
Only supports SHA-256.

Not real-time or automated.

Doesn’t support directories or recursive checking.

👩‍💻 Author
Created by: Abhijit Dash

Project type: Cybersecurity and ethical hacking

📜 License
This project is open-source and free to use for educational purposes.

yaml
Copy
Edit
