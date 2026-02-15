import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

API_KEY = "77bb79c950a17ffb0c27e4d64f73f154"

def get_weather():
    city = city_entry.get()
    unit = unit_var.get()

    if not city:
        messagebox.showerror("Error", "Enter a city")
        return

    units = "metric" if unit == "C" else "imperial"
    symbol = "°C" if unit == "C" else "°F"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}"

    try:
        data = requests.get(url).json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        desc = data["weather"][0]["description"]
        icon_code = data["weather"][0]["icon"]

        # icon
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        img_data = requests.get(icon_url).content
        open("icon.png", "wb").write(img_data)
        img = Image.open("icon.png")
        img = ImageTk.PhotoImage(img)
        icon_label.config(image=img)
        icon_label.image = img

        result_label.config(
            text=f"{city}\n{temp}{symbol}\n{desc.capitalize()}"
        )

        extra_label.config(
            text=f"Humidity: {humidity}%\nWind: {wind} m/s"
        )

    except:
        messagebox.showerror("Error", "Network error")

# ---------- GUI ----------
root = tk.Tk()
root.title("Advanced Weather App")
root.geometry("400x500")
root.configure(bg="#1e1e2f")

# Header
header = tk.Label(
    root, text="WEATHER FORECAST",
    font=("Helvetica", 18, "bold"),
    bg="#6c63ff", fg="white", pady=10
)
header.pack(fill="x")

# Input
city_entry = tk.Entry(root, font=("Arial",14), justify="center")
city_entry.pack(pady=15)
city_entry.insert(0, "Delhi")

# Unit
unit_var = tk.StringVar(value="C")
unit_frame = tk.Frame(root, bg="#1e1e2f")
unit_frame.pack()

tk.Radiobutton(unit_frame, text="Celsius", variable=unit_var, value="C", bg="#1e1e2f", fg="white").pack(side="left")
tk.Radiobutton(unit_frame, text="Fahrenheit", variable=unit_var, value="F", bg="#1e1e2f", fg="white").pack(side="left")

# Button
tk.Button(
    root, text="Get Weather",
    font=("Arial",12,"bold"),
    bg="#00c896", fg="white",
    width=20,
    command=get_weather
).pack(pady=10)

# Icon
icon_label = tk.Label(root, bg="#1e1e2f")
icon_label.pack()

# Result
result_label = tk.Label(
    root, text="", font=("Arial",16,"bold"),
    bg="#1e1e2f", fg="#ffd369"
)
result_label.pack(pady=10)

extra_label = tk.Label(
    root, text="", font=("Arial",12),
    bg="#1e1e2f", fg="white"
)
extra_label.pack()

root.mainloop()

