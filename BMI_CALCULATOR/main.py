import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

# ---------- DATABASE ----------
conn = sqlite3.connect("bmi.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS bmi_records (
    name TEXT,
    weight REAL,
    height REAL,
    bmi REAL,
    category TEXT,
    date TEXT
)
""")
conn.commit()

# ---------- BMI LOGIC ----------
def calculate_bmi():
    name = entry_name.get()
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100
    except:
        messagebox.showerror("Error", "Enter valid numbers")
        return

    if weight <= 0 or height <= 0:
        messagebox.showerror("Error", "Values must be positive")
        return

    bmi = round(weight / (height ** 2), 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    result_label.config(text=f"BMI: {bmi} ({category})")

    cur.execute("INSERT INTO bmi_records VALUES (?,?,?,?,?,?)",
                (name, weight, height*100, bmi, category, datetime.now().strftime("%d-%m-%Y")))
    conn.commit()

# ---------- SHOW HISTORY ----------
def show_history():
    name = entry_name.get()
    cur.execute("SELECT date, bmi FROM bmi_records WHERE name=?", (name,))
    data = cur.fetchall()

    if not data:
        messagebox.showinfo("Info", "No data found")
        return

    dates = [row[0] for row in data]
    bmis = [row[1] for row in data]

    plt.plot(dates, bmis, marker="o")
    plt.title(f"BMI Trend for {name}")
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ---------- GUI ----------
root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("500x450")
root.configure(bg="#1e1e2f")   # dark background

# Header
header = tk.Label(
    root,
    text="BMI HEALTH TRACKER",
    font=("Helvetica", 20, "bold"),
    bg="#6c63ff",
    fg="white",
    pady=10
)
header.pack(fill="x")

# Main Frame
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=30)

label_style = {"font":("Arial",12), "bg":"#1e1e2f", "fg":"white"}
entry_style = {"font":("Arial",12)}

tk.Label(frame, text="Name", **label_style).grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame, **entry_style)
entry_name.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Weight (kg)", **label_style).grid(row=1, column=0, sticky="w")
entry_weight = tk.Entry(frame, **entry_style)
entry_weight.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Height (cm)", **label_style).grid(row=2, column=0, sticky="w")
entry_height = tk.Entry(frame, **entry_style)
entry_height.grid(row=2, column=1, pady=5)

# Buttons
btn_calc = tk.Button(
    root,
    text="Calculate BMI",
    font=("Arial",12,"bold"),
    bg="#00c896",
    fg="white",
    width=20,
    command=calculate_bmi
)
btn_calc.pack(pady=10)

btn_graph = tk.Button(
    root,
    text="Show History Graph",
    font=("Arial",12,"bold"),
    bg="#ff6584",
    fg="white",
    width=20,
    command=show_history
)
btn_graph.pack(pady=5)

# Result
result_label = tk.Label(
    root,
    text="BMI: ",
    font=("Arial",16,"bold"),
    bg="#1e1e2f",
    fg="#ffd369"
)
result_label.pack(pady=20)

root.mainloop()
