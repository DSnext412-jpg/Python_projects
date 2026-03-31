tasks=[]

def show_tasks():
    if not tasks:
        print("NO tasks available")
    else:
        print("\nyour tasks:")
        for i,task in enumerate(tasks,start=1):
            print(f"{i}.{task}")


def add_task():
    task=input("enter task: ").strip()
    if task:
        tasks.append(task)
        print(f"'{task}' added")
    else:
        print("task cannot be empty.")


def delete_task():
    show_tasks()
    if not tasks:
        return
    try:
        index=int(input("enter task number to delete: "))-1
        if 0<=index<len(tasks):
            removed=tasks.pop(index)
            print(f"'{removed}'removed")
        else:
            print("invalid task number")
    except ValueError:
        print("please enter valid number")


def save_tasks():
    with open("tasks.txt","w") as file:
        for task in tasks:
            file.write(task+"\n")


def load_tasks():
    try:
        with open("tasks.txt","r") as file:
            for line in file:
                line=line.strip()
                if line:
                    tasks.append(line)
    except FileNotFoundError:
        pass


load_tasks()
print('\n\n')
while True:
    print("1.view tasks")
    print("2.add task")
    print("3.delete task")
    print("4.exit")
    print('\n\n')

    choice=input("choice: ").strip()

    if choice=="1":
        show_tasks()
    elif choice=="2":
        add_task()
    elif choice=="3":
        delete_task()
    elif choice=="4":
        save_tasks()
        print("tasks saved Bye!")
        break
    else:
        print("Invalid choice try 1–4")