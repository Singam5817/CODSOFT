
todo_list = []

def add_task():
    """Allows the user to add a new task."""
    task = input("Enter the task you want to add: ").strip()
    if task:
        todo_list.append({'task': task, 'done': False})
        print(f"✅ Task added: '{task}'")
    else:
        print("Task cannot be empty.")

def view_tasks():
    """Displays all tasks with their status."""
    if not todo_list:
        print("\nYour To-Do List is empty! Time to add some tasks.")
        return

    print("\n--- Current To-Do List ---")
    for i, item in enumerate(todo_list, 1):
        status = "✓" if item['done'] else " "
        print(f"{i}. [{status}] {item['task']}")
    print("--------------------------")

def mark_done():
    """Allows the user to mark a task as completed (Update/Track)."""
    view_tasks()
    if not todo_list:
        return
    
    try:
        task_num = int(input("Enter the number of the task to mark as DONE: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]['done'] = True
            print(f"🎉 Task {task_num} marked as done!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")


def run_todo_app():
    print("================================")
    print("      Simple To-Do List App     ")
    print("================================")
    
    while True:
        print("\nMenu: 1-Add Task, 2-View List, 3-Mark Done, 4-Exit")
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    run_todo_app()