import os
import tkinter as tk
from tkinter import filedialog

# Create a symlink on the desktop
def create_symlink():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select File")
    if file_path:
        desktop_path = os.path.expanduser('~/Desktop')  # Path to the desktop folder
        symlink_name = os.path.basename(file_path)  # Use the file's name as the symlink name
        symlink_path = os.path.join(desktop_path, symlink_name)

        try:
            os.symlink(file_path, symlink_path)
            print(f"Symlink created: {symlink_path}")
        except Exception as e:
            print(f"Error creating symlink: {e}")

# Create the main window
window = tk.Tk()
window.title("Symlink Creator")

# Create a button to open the file browser and create the symlink
create_button = tk.Button(window, text="Select File and Create Symlink", command=create_symlink)
create_button.pack()

# Start the Tkinter event loop
window.mainloop()
