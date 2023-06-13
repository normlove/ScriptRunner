import tkinter as tk
from tkinter import filedialog
import subprocess
import platform

class TextEditor:
    def __init__(self, root):
        self.root = root
        
        self.create_main_frame()
        self.create_text_editor()
        self.create_terminal()
        self.create_onscreen_keyboard()
        self.create_status_bar()

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def create_text_editor(self):
        self.text_frame = tk.Frame(self.main_frame)
        self.text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.text = tk.Text(self.text_frame)
        self.text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def create_terminal(self):
        self.terminal_frame = tk.Frame(self.main_frame)
        self.terminal_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.terminal_text = tk.Text(self.terminal_frame, bg="black", fg="white")
        self.terminal_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(self.terminal_frame, command=self.terminal_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.terminal_text.config(yscrollcommand=scrollbar.set)

    def create_onscreen_keyboard(self):
        keyboard_frame = tk.Frame(self.root)
        keyboard_frame.pack(side=tk.TOP, padx=5, pady=10)

        # List of keyboard buttons
        button_texts = [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
            ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
            ["z", "x", "c", "v", "b", "n", "m"],
            ["Space", "-", "_", "=", "+", "[", "]", "{", "}", "(", ")"],
            ["<", ">", "/", "\\", "|", ":", ";", "'", '"', "`"],
            ["@", "#", "$", "%", "&", "*", "^", "~", ".", ","],
            ["Caps", "Clear", "Backspace", "Return"]
        ]

        # Variable to track if Caps Lock is on
        self.caps_lock = tk.BooleanVar(value=False)

        for row, button_row in enumerate(button_texts):
            for col, button_text in enumerate(button_row):
                if button_text == "Space":
                    button = tk.Button(keyboard_frame, text=button_text, width=10, height=2,
                                       command=lambda text=button_text: self.insert_text(" "))
                elif button_text == "Return":
                    button = tk.Button(keyboard_frame, text=button_text, width=10, height=2,
                                       command=lambda: self.insert_text("\n"))
                else:
                    button = tk.Button(keyboard_frame, text=button_text, width=5, height=2,
                                       command=lambda text=button_text: self.insert_text(text))
                button.grid(row=row, column=col, padx=2, pady=2)

        caps_button = tk.Button(keyboard_frame, text="Caps", width=5, height=2,
                                command=self.toggle_caps_lock)
        caps_button.grid(row=7, column=0, padx=2, pady=2)

        clear_button = tk.Button(keyboard_frame, text="Clear", width=5, height=2,
                                 command=self.clear_text)
        clear_button.grid(row=7, column=1, padx=2, pady=2)

        backspace_button = tk.Button(keyboard_frame, text="Backspace", width=10, height=2,
                                     command=self.delete_text)
        backspace_button.grid(row=7, column=2, padx=2, pady=2)

        run_button = tk.Button(keyboard_frame, text="Run in Terminal", width=18, height=2,
                               command=self.run_in_terminal)
        run_button.grid(row=8, column=0, columnspan=3, padx=2, pady=2)

        save_button = tk.Button(keyboard_frame, text="Save", width=10, height=2,
                                command=self.save_file)
        save_button.grid(row=8, column=3, padx=2, pady=2)

        open_button = tk.Button(keyboard_frame, text="Open", width=10, height=2,
                                command=self.open_file)
        open_button.grid(row=8, column=4, padx=2, pady=2)

    def create_status_bar(self):
        self.status_var = tk.StringVar()
        self.status_var.set("Uppercase: OFF")
        status_label = tk.Label(self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def insert_text(self, text):
        current_text = self.text.get(tk.INSERT)
        if self.caps_lock.get():
            text = text.upper()
        self.text.insert(tk.INSERT, text)

    def toggle_caps_lock(self):
        self.caps_lock.set(not self.caps_lock.get())
        if self.caps_lock.get():
            self.status_var.set("Uppercase: ON")
        else:
            self.status_var.set("Uppercase: OFF")

    def clear_text(self):
        self.text.delete("1.0", tk.END)

    def delete_text(self):
        self.text.delete("insert-1c", tk.INSERT)

    def new_file(self):
        self.text.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, file.read())

    def save_file(self):
        current_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if current_file:
            with open(current_file, "w") as file:
                file.write(self.text.get("1.0", tk.END))

    def run_in_terminal(self):
        current_text = self.text.get("1.0", tk.END).strip()
        if current_text:
            process = subprocess.Popen(["bash", "-c", current_text], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       stdin=subprocess.PIPE)

            output, error = process.communicate()
            if output:
                self.terminal_text.insert(tk.END, output.decode())
            if error:
                self.terminal_text.insert(tk.END, error.decode())

root = tk.Tk()
root.title("TextermPi by normanlove")
editor = TextEditor(root)

# Set the size of the terminal and text editor frames to be the same
editor.text_frame.config(width=50, height=20)
editor.terminal_frame.config(width=50, height=20)

root.mainloop()
