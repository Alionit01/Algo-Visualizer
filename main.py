import tkinter as tk
from tkinter import ttk, messagebox
from data_generator import generate_records

records = generate_records(1000)

# --- GUI ---
root = tk.Tk()
root.title("DSA Sorting & Searching App")
root.geometry("800x600")

# Treeview to show data
tree = ttk.Treeview(root, columns=("ID", "Name", "Age"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.pack(fill=tk.BOTH, expand=True)

# Load data to Tree
def load_data():
    for row in tree.get_children():
        tree.delete(row)
    for rec in records:
        tree.insert("", tk.END, values=(rec["id"], rec["name"], rec["age"]))

load_data()

root.mainloop()
