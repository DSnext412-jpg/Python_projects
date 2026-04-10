import json
students=[]
def add_student():
    name=input("enter student name ").strip()
    try:
        marks=float(input("enter marks:"))
        students.append({"name":name,"marks":marks})
        print("student added success")
    except ValueError:
        print("invalid marks! enter a number.")

def show_students():
    if not students:
        print("no students found")
    else:
        print("\nstudent List:")
        for i,s in enumerate(students,start=1):
            print(f"{i}.{s['name']}-{s['marks']}")

def search_student():
    name=input("enter name to search:").strip().lower()
    found=False

    for s in students:
        if s["name"].lower()==name:
            print(f"Found:{s['name']}-{s['marks']}")
            found=True

    if not found:
        print("Student not found")

def save_students():
    with open("students.json","w") as file:
        json.dump(students,file,indent=4)

def load_students():
    try:
        with open("students.json","r") as file:
            data=json.load(file)
            students.extend(data)
    except FileNotFoundError:
        pass
load_students()

while True:
    print("1. Add Student")
    print("2. view Students")
    print("3. Search Student")
    print("4. exit")
    choice=input("Enter choice:")

    if choice=="1":
        add_student()
    elif choice=="2":
        show_students()
    elif choice=="3":
        search_student()
    elif choice=="4":
        save_students()
        print("data saved exiting")
        break
    else:
        print("invalid choice")
