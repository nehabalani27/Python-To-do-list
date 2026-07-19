tasks = []


def show_tasks():
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. [{status}] {task['title']}")
        print()


while True:
    print("===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        title = input("Enter task: ")
        tasks.append({"title": title, "completed": False})
        print("Task added successfully!\n")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        if tasks:
            try:
                task_no = int(input("Enter task number to mark as completed: "))
                tasks[task_no - 1]["completed"] = True
                print("Task marked as completed!\n")
            except (ValueError, IndexError):
                print("Invalid task number.\n")

    elif choice == "4":
        show_tasks()
        if tasks:
            try:
                task_no = int(input("Enter task number to delete: "))
                deleted = tasks.pop(task_no - 1)
                print(f"Deleted: {deleted['title']}\n")
            except (ValueError, IndexError):
                print("Invalid task number.\n")

    elif choice == "5":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.\n")