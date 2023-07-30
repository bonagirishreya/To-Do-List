class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):    
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found!")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")

def display_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Exit")

def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added successfully!")

        elif choice == '2':
            task = input("Enter the task you want to remove: ")
            todo_list.remove_task(task)

        elif choice == '3':
            todo_list.show_tasks()

        elif choice == '4':
            print("Exiting the To-Do List application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
