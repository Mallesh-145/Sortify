import tkinter as tk
from tkinter import messagebox
import base  # Your existing script
import Organiser
import config

root = tk.Tk()
root.title("Sortify ")
root.geometry("600x400")  # Set width x height

# Optional: Set icon (make sure you have .ico file)
# root.iconbitmap('sortify.ico')

# Title label
title_label = tk.Label(root, text="Welcome to Sortify", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Buttons
def scan_files():
    messagebox.showinfo("Scan", "Scanning Downloads Folder...")
    base.run()  # We'll turn base.py into a function-friendly module

def organise_files():
    messagebox.showinfo("Organise", "Organising files now...")
    Organiser.run()  # Same here, we’ll modularize organiser.py

def create_folders():
    config.create_folders()
    messagebox.showinfo("Folders", "Folders checked and created.")

scan_button = tk.Button(root, text=" Scan Downloads", command=scan_files)
scan_button.pack(pady=5)

organise_button = tk.Button(root, text=" Organise Files", command=organise_files)
organise_button.pack(pady=5)

create_button = tk.Button(root, text=" Create Folders", command=create_folders)
create_button.pack(pady=5)

root.mainloop()

