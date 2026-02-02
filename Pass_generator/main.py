import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------- LOGIC ----------
def generate_password():
    try:
        length = int(length_entry.get())
    except:
        messagebox.showerror("Error", "Length must be a number")
        return

    if length < 6 or length > 50:
        messagebox.showerror("Error", "Length should be between 6 and 50")
        return

    charset = ""

    if var_upper.get():
        charset += string.ascii_uppercase
    if var_lower.get():
        charset += string.ascii_lowercase
    if var_numbers.get():
        charset += string.digits
    if var_symbols.get():
        charset += string.punctuation

    exclude = exclude_entry.get()
    for ch in exclude:
        charset = charset.replace(ch, "")

    if not charset:
        messagebox.showerror("Error", "Select at least one character type")
        return

    password = "".join(random.choice(charset) for _ in range(length))

    # Security rules
    if length >= 12 and var_upper.get() and var_lower.get() and var_numbers.get() and var_symbols.get():
        strength = "Strong"
        color = "green"
    elif length >= 8:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Weak"
        color = "red"

    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)
    strength_label.config(text=f"Strength: {strength}", fg=color)

def copy_to_clipboard():
    pwd = result_entry.get()
    if not pwd:
        return
    root.clipboard_clear()
    root.clipboard_append(pwd)
    messagebox.showinfo("Copied", "Password copied to clipboard")

# ---------- GUI ----------
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("500x450")
root.configure(bg="#1e1e2f")

# Header
header = tk.Label(
    root,
    text="SECURE PASSWORD GENERATOR",
    font=("Helvetica", 18, "bold"),
    bg="#6c63ff",
    fg="white",
    pady=10
)
header.pack(fill="x")

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=20)

label_style = {"bg":"#1e1e2f", "fg":"white", "font":("Arial",11)}

tk.Label(frame, text="Password Length", **label_style).grid(row=0, column=0, sticky="w")
length_entry = tk.Entry(frame)
length_entry.grid(row=0, column=1)
length_entry.insert(0, "12")

# Options
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(frame, text="Uppercase (A-Z)", variable=var_upper, **label_style).grid(row=1, column=0, columnspan=2, sticky="w")
tk.Checkbutton(frame, text="Lowercase (a-z)", variable=var_lower, **label_style).grid(row=2, column=0, columnspan=2, sticky="w")
tk.Checkbutton(frame, text="Numbers (0-9)", variable=var_numbers, **label_style).grid(row=3, column=0, columnspan=2, sticky="w")
tk.Checkbutton(frame, text="Symbols (!@#)", variable=var_symbols, **label_style).grid(row=4, column=0, columnspan=2, sticky="w")

# Exclude
tk.Label(frame, text="Exclude characters", **label_style).grid(row=5, column=0, sticky="w")
exclude_entry = tk.Entry(frame)
exclude_entry.grid(row=5, column=1)

# Buttons
tk.Button(
    root, text="Generate Password",
    font=("Arial",12,"bold"),
    bg="#00c896", fg="white",
    width=25,
    command=generate_password
).pack(pady=10)

# Result
result_entry = tk.Entry(root, font=("Consolas",14), width=30, justify="center")
result_entry.pack(pady=10)

strength_label = tk.Label(root, text="Strength: ", font=("Arial",12,"bold"), bg="#1e1e2f")
strength_label.pack()

tk.Button(
    root, text="Copy to Clipboard",
    font=("Arial",11,"bold"),
    bg="#ff6584", fg="white",
    width=20,
    command=copy_to_clipboard
).pack(pady=10)

root.mainloop()
