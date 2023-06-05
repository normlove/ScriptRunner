import tkinter as tk
from tkinter import filedialog
import shutil
import subprocess

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(tk.END, file_path)

def browse_destination():
    destination_path = filedialog.askdirectory()
    if destination_path:
        destination_entry.delete(0, tk.END)
        destination_entry.insert(tk.END, destination_path)

def copy_file():
    file_path = file_entry.get()
    destination = destination_entry.get()

    # Use sudo to copy the file with elevated permissions
    subprocess.run(['sudo', 'cp', file_path, destination])

    status_label.config(text="File copied successfully!")

root = tk.Tk()
root.title("File Copier")

# Create the file selection button
file_button = tk.Button(root, text="Select File", command=browse_file)
file_button.pack()

# Create the file entry
file_entry = tk.Entry(root, width=50)
file_entry.pack()

# Create the destination selection button
destination_button = tk.Button(root, text="Select Destination", command=browse_destination)
destination_button.pack()

# Create the destination entry
destination_entry = tk.Entry(root, width=50)
destination_entry.pack()

# Create the status label
status_label = tk.Label(root, text="", fg="green")
status_label.pack()

# Create the copy button
copy_button = tk.Button(root, text="Copy File", command=copy_file)
copy_button.pack()

root.mainloop()
