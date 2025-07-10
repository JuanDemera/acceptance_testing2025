import uuid
from datetime import datetime

class Task:
    def __init__(self, title, description='', due_date=None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.due_date = due_date if due_date else None
        self.completed = False
        self.created_at = datetime.now()

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{self.id}] {self.title} - {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []
        print("ToDo list created!")

    def add_task(self, task: Task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added!")

    def list_tasks(self):
        if not self.tasks:
            print("No hay tareas.")
        else:
            print("\n--- Task List ---")
            for task in self.tasks:
                print(task)
        return self.tasks

    def mark_task_completed(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.mark_complete()
                print(f"Task '{task.title}' marked as completed!")
                return "Task marked as completed."
        print("Task not found")
        return "Task not found"

    def clear_all_tasks(self):
        self.tasks.clear()
        print("All tasks cleared!")

    def update_task_title(self, old_title, new_title):
        for task in self.tasks:
            if task.title == old_title:
                task.title = new_title
                print(f"Task title updated from '{old_title}' to '{new_title}'")
                return "Task updated."
        print("Task not found")
        return "Task not found"

# ----------- MENÚ INTERACTIVO -----------

def print_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar todas las tareas")
    print("5. Actualizar título de una tarea")
    print("6. Salir")

def main():
    todo_list = ToDoList()

    while True:
        print_menu()
        choice = input("Selecciona una opción: ")

        if choice == '1':
            title = input("Título de la tarea: ")
            description = input("Descripción (opcional): ")
            task = Task(title=title, description=description)
            todo_list.add_task(task)

        elif choice == '2':
            todo_list.list_tasks()

        elif choice == '3':
            title = input("Título de la tarea a marcar como completada: ")
            todo_list.mark_task_completed(title)

        elif choice == '4':
            confirm = input("¿Seguro que quieres borrar todas las tareas? (s/n): ")
            if confirm.lower() == 's':
                todo_list.clear_all_tasks()

        elif choice == '5':
            old_title = input("Título actual de la tarea: ")
            new_title = input("Nuevo título para la tarea: ")
            todo_list.update_task_title(old_title, new_title)

        elif choice == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
