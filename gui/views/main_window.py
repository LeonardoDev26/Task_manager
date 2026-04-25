import tkinter as tk
from services.task_service import get_tasks

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.root.geometry("400x400")

        self.task_listbox = tk.Listbox(self.root, width=50)
        self.task_listbox.pack(pady=20)

        self.load_tasks()

    def load_tasks(self):
        tasks = get_tasks()

        for task in tasks:
            self.task_listbox.insert(tk.END, task[1])

    def run(self):
        self.root.mainloop()

