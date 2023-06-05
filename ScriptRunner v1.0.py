import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from subprocess import Popen, PIPE

SCRIPTS_FOLDER = "Scripts"  # Name of the folder containing the scripts

def run_script():
    selected_script = script_var.get()
    script_path = os.path.join(script_folder_path, selected_script)
    process = Popen(['python', script_path], stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    if process.returncode == 0:
        print("Script executed successfully!")
    else:
        print("Error executing script:", error.decode())

def scan_folder():
    script_files = [f for f in os.listdir(script_folder_path) if f.endswith('.py')]

    script_dropdown['menu'].delete(0, 'end')  # Clear previous options

    # Add scripts to dropdown menu
    for script_file in script_files:
        label = os.path.splitext(script_file)[0]
        script_dropdown['menu'].add_command(label=label, command=tk._setit(script_var, script_file))

def select_script():
    script_file = filedialog.askopenfilename(filetypes=[("Python Scripts", "*.py")])
    if script_file:
        script_name = os.path.basename(script_file)
        dest_path = os.path.join(script_folder_path, script_name)
        shutil.copy2(script_file, dest_path)
        script_var.set(script_name)
        scan_folder()

def delete_script():
    selected_script = script_var.get()
    if selected_script:
        script_path = os.path.join(script_folder_path, selected_script)
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete '{selected_script}'?"):
            os.remove(script_path)
            script_var.set("")
            scan_folder()

# Determine the path of the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
script_folder_path = os.path.join(script_dir, SCRIPTS_FOLDER)

root = tk.Tk()
root.title("ScriptRunner v1.0")

# Dropdown menu to select the script
script_var = tk.StringVar(root)
script_label = tk.Label(root, text="Select a script: ")
script_label.grid(row=0, column=0, padx=10, pady=10)
script_dropdown = tk.OptionMenu(root, script_var, '')
script_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# Execute button
execute_button = tk.Button(root, text="Execute Script", command=run_script)
execute_button.grid(row=1, column=0, padx=10, pady=10, sticky='we')

# Install Script button
install_button = tk.Button(root, text="Install Script", command=select_script)
install_button.grid(row=1, column=1, padx=10, pady=10, sticky='we')

# Delete Script button
delete_button = tk.Button(root, text="Delete Script", command=delete_script)
delete_button.grid(row=2, column=0, padx=10, pady=10, sticky='we', columnspan=2)

# Label for program title at the bottom center
title_label = tk.Label(root, text="ScriptRunner v1.0 by normanlove")
title_label.grid(row=3, column=0, columnspan=2, pady=10, sticky='we')

# Scan the script folder
scan_folder()

root.mainloop()
