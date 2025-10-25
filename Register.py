import tkinter as tk
from tkinter import messagebox
import sqlite3

# ----- DATABASE SETUP -----
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# ----- REGISTER FUNCTION -----
def register_user():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not name or not email or not password:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, password))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Registration successful!")

        # Clear fields after successful registration
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email already exists.")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# ----- GUI SETUP -----
root = tk.Tk()
root.title("User Registration Form")
root.geometry("350x300")

# Initialize DB
init_db()

# Name
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Email
tk.Label(root, text="Email:").pack(pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

# Password
tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show='*', width=30)
password_entry.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Register", command=register_user)
submit_button.pack(pady=20)

root.mainloop()
