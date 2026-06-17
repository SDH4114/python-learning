import json
from pathlib import Path

def load_students():
    try:
        with open(Path(__file__).parent / "students.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File didnt find")
        return []
    except json.decoder.JSONDecodeError:
        print("File is empty or broken")
        return []

def save_students(students):
    with open(Path(__file__).parent / "students.json", "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)




def add_student(students):
    print("Write student's name.")
    name = input("> ").capitalize()

    student = {
        "name": name,
        "subjects": {}
    }

    while True:
        print("Write subject or stop:")
        subject = input("> ").capitalize()
        if subject.lower() == "stop":
            break

        if subject not in student["subjects"]:
            student["subjects"][subject] = []

        while True:
            try:
                print("Write mark:")
                mark = int(input("> "))
                student["subjects"][subject].append(mark)
                break

            except ValueError:
                print("Write number.")

    students.append(student)
    save_students(students)
    print("Student added.")





def menu():
    students = load_students()

    print("""
Student Grade Analyzer

1. Add student
2. Add grade
3. Show students
4. Show student grades
5. Show student average
6. Show subject average
7. Show best student
8. Exit
""")

    chooseDo= input("> ").lower()
    while True:
        if chooseDo in ("add student", "add", "1"):
            add_student(students)
            input("Waiting...")

        elif chooseDo in ("exit", "8"):
            break
        else:
            print("Unknown command")


if __name__ == "__main__":
    menu()