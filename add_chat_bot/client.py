import socket, threading, tkinter as tk
from cryptography.fernet import Fernet
from tkinter import simpledialog

# --------- ENCRYPTION ---------
KEY = b'gpRXckyXQyeRtZVEY_1e6U7TVR8iqHhT7d13KmsMrtQ='
cipher = Fernet(KEY)

# --------- SOCKET ---------
client = socket.socket()
client.connect(("127.0.0.1", 5000))

# --------- USERNAME ---------
root = tk.Tk()
root.withdraw()
username = simpledialog.askstring("Username", "Enter your name:")
root.deiconify()

# --------- RECEIVE ---------
def receive():
    while True:
        try:
            msg = cipher.decrypt(client.recv(2048)).decode()
            chat.insert(tk.END, msg + "\n")
            chat.see(tk.END)
            root.bell()
        except:
            break

# --------- SEND ---------
def send():
    msg = entry.get()
    if msg:
        full_msg = f"{username}: {msg}"
        client.send(cipher.encrypt(full_msg.encode()))
        entry.delete(0, tk.END)

# --------- GUI ---------
root.title("Advanced Chat App")
root.geometry("500x600")
root.configure(bg="#1e1e2f")

header = tk.Label(
    root,
    text="Secure Chat Application",
    font=("Helvetica", 18, "bold"),
    bg="#6c63ff",
    fg="white",
    pady=10
)
header.pack(fill="x")

chat_frame = tk.Frame(root, bg="#1e1e2f")
chat_frame.pack(pady=10, padx=10, fill="both", expand=True)

scroll = tk.Scrollbar(chat_frame)
scroll.pack(side="right", fill="y")

chat = tk.Text(
    chat_frame,
    yscrollcommand=scroll.set,
    font=("Segoe UI Emoji", 11),
    bg="#2a2a3d",
    fg="white",
    wrap="word"
)
chat.pack(fill="both", expand=True)
scroll.config(command=chat.yview)

entry_frame = tk.Frame(root, bg="#1e1e2f")
entry_frame.pack(fill="x", padx=10, pady=10)

entry = tk.Entry(entry_frame, font=("Arial", 12))
entry.pack(side="left", fill="x", expand=True, padx=(0,10))

send_btn = tk.Button(
    entry_frame,
    text="Send",
    font=("Arial", 11, "bold"),
    bg="#00c896",
    fg="white",
    width=10,
    command=send
)
send_btn.pack(side="right")

status = tk.Label(
    root,
    text="Connected to server",
    bg="#1e1e2f",
    fg="#00c896",
    anchor="w"
)
status.pack(fill="x", padx=10, pady=(0,5))

threading.Thread(target=receive, daemon=True).start()
root.mainloop()
