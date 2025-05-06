import tkinter as tk
from tkinter import messagebox
import re

def check_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    if length_error:
        return "Weak (too short)"
    elif digit_error or uppercase_error or lowercase_error or symbol_error:
        return "Moderate"
    else:
        return "Strong"

def evaluate_password():
    password = password_entry.get()
    strength = check_strength(password)
    result_label.config(text=f"Password Strength: {strength}")
    if strength == "Strong":
        result_label.config(fg="green")
    elif strength == "Moderate":
        result_label.config(fg="orange")
    else:
        result_label.config(fg="red")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
password_entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
password_entry.pack()

tk.Button(root, text="Check Strength", command=evaluate_password, font=("Arial", 12)).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
