import tkinter as tk
from tkinter import filedialog
import subprocess

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")

        # Create a Text widget
        self.text_widget = tk.Text(root)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        # Create a Menu bar
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Run", command=self.run_pro)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.destroy)

        # Initialize file path
        self.file_path = None

    def new_file(self):
        # Clear the Text widget
        self.text_widget.delete(1.0, tk.END)
        # Reset the file path
        self.file_path = None

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)
            self.file_path = file_path

    def save_file(self):
        if self.file_path:
            content = self.text_widget.get(1.0, tk.END)
            with open(self.file_path, "w") as file:
                file.write(content)
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
        if file_path:
            content = self.text_widget.get(1.0, tk.END)
            with open(file_path, "w") as file:
                file.write(content)
            self.file_path = file_path


    def run_pro(self):
        print(self.file_path)
        subprocess.run(["python", "-u", self.file_path]) 



if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()