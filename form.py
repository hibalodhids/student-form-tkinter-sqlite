import tkinter as tk
from tkinter import messagebox
import sqlite3


class StudentForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Form")
        self.root.geometry("500x400")

        # Database connection
        self.conn = sqlite3.connect("students.db")
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS student (
                name TEXT,
                age INT,
                gender TEXT,
                email TEXT
            )
        """)

        #label
        labels = ["Name", "Age", "Gender", "Email"]
        self.entries = {}

        for i, text in enumerate(labels):
            tk.Label(root, text=text).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(root)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[text.lower()] = entry

        # Buttons
        tk.Button(root, text="Submit", command=self.save).grid(row=5, column=0, pady=20)
        tk.Button(root, text="Show Records", command=self.show).grid(row=5, column=1, pady=20)

    def save(self):
        data = tuple(e.get() for e in self.entries.values())
        if all(data):
            self.conn.execute("INSERT INTO student VALUES (?, ?, ?, ?)", data)
            self.conn.commit()
            messagebox.showinfo("Saved", "Data inserted successfully!")
            for e in self.entries.values():
                e.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "All fields are required!")

    def show(self):
        rows = self.conn.execute("SELECT * FROM student").fetchall()
        if rows:
            messagebox.showinfo("Records", "\n".join(str(r) for r in rows))
        else:
            messagebox.showinfo("Records", "No data found.")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentForm(root)
    root.mainloop()



