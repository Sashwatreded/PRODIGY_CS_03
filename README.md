# 🔐 Password Strength Checker Tool (Python GUI)

This project is a **Password Strength Checker Tool** developed using Python and Tkinter.  
Built as part of my internship at **Prodigy Infotech**, the tool helps users evaluate the strength of their passwords based on common security rules.

It provides **instant feedback** on password quality — encouraging the use of strong, secure passwords.

---

## 🚀 Features

- GUI-based password input
- Real-time strength evaluation
- Visual feedback (Weak, Moderate, Strong)
- Checks for:
  - Minimum length
  - Use of uppercase and lowercase letters
  - Digits
  - Special characters

---

## 🛠️ Tech Stack

- Python
- `Tkinter` for GUI
- `re` (Regular Expressions) for pattern matching

---

## 📋 How It Works

1. **Enter a password** in the input field.
2. The tool checks for:
   - Length (at least 8 characters)
   - Uppercase & lowercase letters
   - Digits (0–9)
   - Special characters (e.g. !, @, #, etc.)
3. **Strength levels** are evaluated and displayed as:
   - 🔴 Weak
   - 🟡 Moderate
   - 🟢 Strong

4. User receives a recommendation message to improve password security.

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-strength-checker.git
   cd password-strength-checker
