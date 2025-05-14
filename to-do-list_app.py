#------------------------To Do List App------------------------------

tasks = []

def add_task(task_name, priority):
    print("----Adding task----")
    task = {
        "title" : task_name,
        "completed" : "No",
        "priority" : priority
    }
    tasks.append(task)
    print(f"{task_name} added successfully....✅")

def delete_task(index):
    print("----Deleting task----")
    if index >= 0 and len(tasks) > index:
        del tasks[index]
        print("Task deleted successfully....✅")
    else:
        print("You entered inavlid task❌ or there is no tasks🙄")

def show_task():
    print("----Showing task----")
    if not tasks:
        print("No task yet...❌")
    else:
        for task in range(len(tasks)):
            tsk = tasks[task]
            print(f"Target is '{tsk['title']}'. Its priority is on {tsk['priority']} number. Completed :'{tsk['completed']}' ")

def update_task(index, update_key, update_value):
    if update_key in tasks[index]:
        if index >= 0:
            print("----Updating task----")
            tasks[index][update_key] = update_value
            print("Updated successfully....✅")
        else:
            print("Invalid task...❌")

def completed_task():
    print("-------Completed task-------")

    for task in range(len(tasks)):
        if tasks[task]['completed'] == "Yes":
            print(f"{tasks[task]['title']} is completed ✅")
        else:
            print(f"{tasks[task]['title']} is not completed yet...❌")

def main_menu():
    print("----------------Welcome----------------")

    while True:
        print("1 -- Add task")
        print("2 -- Delete task")
        print("3 -- Update task")
        print("4 -- Show task")
        print("5 -- See completed task")
        print("6 -- Exit")
        choice = int(input("Enter your choice... : "))

        match choice:
            case 1:
                title = input("Enter the task title... : ").capitalize()
                priority = int(input("What is the priority of this task... : "))
                add_task(title, priority)
            case 2:
                index = int(input("Enter the index of the task... : "))-1
                delete_task(index)
            case 3:
                index = int(input("Enter the index of the task... : "))-1
                key = input("Enter the key which value you want to change... : ").lower()
                value = input("Enter the value of that key... : ").capitalize()
                update_task(index, key, value)
            case 4:
                show_task()
            case 5:
                completed_task() 
            case 6:
                print("Goodbye...😔")
                return
            case _:
                print("Inavlid choice")


main_menu()