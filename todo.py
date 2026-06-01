TASK_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display tasks
def view_tasks(tasks):
    print("\n" + "=" * 40)
    print("           YOUR TASKS")
    print("=" * 40)

    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        print(f"\nTotal Tasks: {len(tasks)}")

tasks = load_tasks()

while True:
    print("\n" + "=" * 40)
    print("      TO-DO LIST APPLICATION")
    print("=" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Search Task")
    print("5. Clear All Tasks")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    # Add Task
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added successfully!")

    # View Tasks
    elif choice == "2":
        view_tasks(tasks)

    # Remove Task
    elif choice == "3":
        view_tasks(tasks)

        if tasks:
            try:
                num = int(input("\nEnter task number to remove: "))
                removed_task = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"🗑 Removed: {removed_task}")
            except:
                print("❌ Invalid task number!")

    # Search Task
    elif choice == "4":
        keyword = input("Enter keyword to search: ").lower()

        found = False
        for task in tasks:
            if keyword in task.lower():
                print("🔍 Found:", task)
                found = True

        if not found:
            print("No matching task found.")

    # Clear All Tasks
    elif choice == "5":
        confirm = input(
            "Are you sure you want to delete all tasks? (yes/no): "
        )

        if confirm.lower() == "yes":
            tasks.clear()
            save_tasks(tasks)
            print("🧹 All tasks cleared successfully!")

    # Exit
    elif choice == "6":
        print("\nThank you for using To-Do List App!")
        print("Goodbye 👋")
        break

    else:
        print("❌ Invalid choice! Please try again.")
        