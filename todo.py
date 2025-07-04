def show_menu():
    print("\n=== To-Do List Menu ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("=====================")

def add_task(tasks):
    task = input("Enter your task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in your to-do list!")
        return
    
    print("\nYour To-Do List:")
    for index, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else " "
        print(f"{index}. [{status}] {task['task']}")

def mark_complete(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Deleted task: {deleted_task['task']}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    tasks = []
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main() 