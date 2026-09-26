# Student Task Manager Project

#  list to store all tasks in memory
tasks = []

def load_tasks():
    #read task from file
    try:
        file = open("tasks.txt", "r")
        lines = file.readlines()
        file.close()
        
        for line in lines:
            line = line.strip()
            if line != "":
                # Split the data
                parts = line.split("|")
                if len(parts) == 4:
                    task = { "id": int(parts[0]),
                        "title": parts[1],
                        "priority": parts[2],
                        "status": parts[3]
                    }
                    tasks.append(task)
        print("Data loaded successfully from tasks.txt!")
    except FileNotFoundError:
        # If file does not exist, create an empty one
        file = open("tasks.txt", "w")
        file.close()

def save_tasks_to_file():
    # save all tasks in file
    file = open("tasks.txt", "w")
    for task in tasks:
        line = str(task["id"]) + "|" + task["title"] + "|" + task["priority"] + "|" + task["status"] + "\n"
        file.write(line)
    file.close()
     
def add_task():
    print("\n  ADD NEW TASK ")
    title = input("Enter task title: ").strip()
    
    if title == "":
        print("Error: Task title cannot be empty!")
        return

    print("Select Priority Level:")
    print("1. High")
    print("2. Medium")
    print("3. Low")
    p_choice = input("Enter choice (1-3): ").strip()
    
    if p_choice == "1":
        priority = "High"
    elif p_choice == "2":
        priority = "Medium"
    elif p_choice == "3":
        priority= "Low"
    
    else:
        print("invalid choice!")
        return

    # Generate a unique task ID
    if len(tasks) == 0:
        task_id = 1
    else:
        task_id = tasks[-1]["id"] + 1

    new_task = {
        "id": task_id,
        "title": title,
        "priority": priority,
        "status": "Pending"
    }

    tasks.append(new_task)
    save_tasks_to_file()
    print("Task added successfully!")


def view_all_tasks():
    print("\n")
    print("ID   | Priority | Status      | Task Title")
    print("")
    if len(tasks) == 0:
        print("No tasks found. Add some tasks first!")
    else:
        for t in tasks:
            print(str(t["id"]) + "    | " + t["priority"] + "     | " + t["status"] + "     | " + t["title"])
    print(" ")


def delete_task():
    print("\nDELETE TASK ")
    view_all_tasks()
    if len(tasks) == 0:
        return

    try:
        task_id = int(input("Enter the ID of the task to delete: "))
    except ValueError:
        print("Error: Please enter a valid numerical ID!")
        return

    found = False
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            found = True
            break

    if found:
        save_tasks_to_file()
        print("Task deleted successfully!")
    else:
        print("Error: Task ID not found.")


def mark_task_complete():
    print("\n MARK TASK AS COMPLETE ")
    view_all_tasks()
    if len(tasks) == 0:
        return

    try:
        task_id = int(input("Enter Task ID to mark as Completed: "))
    except ValueError:
        print("Error: Please enter a valid numerical ID!")
        return

    found = False
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "Completed"
            found = True
            break

    if found:
        save_tasks_to_file()
        print("Task status updated to Completed!")
    else:
        print("Error: Task ID not found.")


def filter_by_priority():
    print("\nFILTER TASKS BY PRIORITY ")
    print("1. High")
    print("2. Medium")
    print("3. Low")
    p_choice = input("Select Priority (1-3): ").strip()

    if p_choice == "1":
        target = "High"
    elif p_choice == "2":
        target = "Medium"
    elif p_choice == "3":
        target = "Low"
    else:
        print("Invalid choice!")
        return

    print("\n")
    print("ID   | Priority | Status      | Task Title")
    count = 0
    for t in tasks:
        if t["priority"] == target:
            print(str(t["id"]) + "    | " + t["priority"] + "     | " + t["status"] + "     | " + t["title"])
            count += 1
            
    if count == 0:
        print("No tasks found with " + target + " priority.")

def main():
    # Load data from file at the start of program
    load_tasks()

    while True:
        print("\n")
        print("   STUDENT TASK MANAGER SYSTEM   ")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Mark Task as Complete")
        print("4. Filter Tasks by Priority")
        print("5. Delete Task")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_all_tasks()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            filter_by_priority()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Saving data... Thank you for using Student Task Manager!")
            break
        else:
            print("Invalid input! Please enter a choice between 1 and 6.")


main()