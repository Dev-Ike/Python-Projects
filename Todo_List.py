tasks = []

while True:
    print("\n1. Add task")
    print("2. Remove task")
    print("3. Mark task as completed")
    print("4. View tasks")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append({"task": task, "completed": False})
    elif choice == "2":
        task_number = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_number < len(tasks):
            del tasks[task_number]
        else:
            print("Invalid task number")
    elif choice == "3":
        task_number = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = True
        else:
            print("Invalid task number")
    elif choice == "4":
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Uncompleted"
            print(f"{i}. {task['task']} - {status}")
    elif choice == "5":
        break
    else:
        print("Invalid choice")