import tkinter as tk
from services.task_service import get_tasks, create_task, delete_task


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.root.geometry("400x400")

        # INPUTS
        self.title_entry = tk.Entry(self.root, width=40)
        self.title_entry.pack(pady=5)

        self.description_entry = tk.Entry(self.root, width=40)
        self.description_entry.pack(pady=5)

        self.date_entry = tk.Entry(self.root, width=40)
        self.date_entry.pack(pady=5)

        # BOTÓN AGREGAR
        self.add_button = tk.Button(
            self.root, text="Agregar tarea", command=self.add_task
        )
        self.add_button.pack(pady=10)

        # BOTÓN ELIMINAR
        self.delete_button = tk.Button(
            self.root, text="Eliminar tarea", command=self.delete_task
        )
        self.delete_button.pack(pady=5)

        # LISTA
        self.task_listbox = tk.Listbox(self.root, width=50)
        self.task_listbox.pack(pady=20)

        # Cargar tareas
        self.load_tasks()

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)  # limpiar antes de cargar
        tasks = get_tasks()

        for task in tasks:
            self.task_listbox.insert(tk.END, f"{task[0]} - {task[1]}")

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        date = self.date_entry.get()

        if not title:
            return  # evitar tareas vacías

        create_task(title, description, date)

        self.load_tasks()

        # limpiar inputs
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def delete_task(self):
        selected = self.task_listbox.curselection()

        if not selected:
            return  # si no hay selección, no hace nada

        index = selected[0]
        task_text = self.task_listbox.get(index)

        # obtener ID
        task_id = int(task_text.split(" - ")[0])

        delete_task(task_id)

        self.load_tasks()

    def run(self):
        self.root.mainloop()