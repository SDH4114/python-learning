import json
from pathlib import Path

def load_students():
    try:
        with open(Path(__file__).parent / "students.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File didnt find")
        return {}
    except json.decoder.JSONDecodeError:
        print("File is empty or broken")
        return {}

def save_students(students):
    with open(Path(__file__).parent / "students.json", "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)


def wait():
    print()
    input("Waiting...")
    print()

def add_student(students):
    print("Write student's name.")
    while True:
        name = input("> ").capitalize()
        if name.isdigit():
            print("Write name not number")
        else:
            break

    if name not in students:
        students[name]= {}

    while True:
        print("Write subject or stop:")
        while True:
            subject = input("> ").lower()
            if subject.isdigit():
                print("Write sentence not number")
            else:
                break

        if subject.lower() == "stop":
            break

        if subject not in students[name]:
            students[name][subject] = []

        while True:
            try:
                print("Write mark")
                mark = int(input("> "))
                if mark >=0 and mark <= 100:
                    students[name][subject].append(mark)
                    break
                else:
                    print("Mark should be from 0 to 100")

            except ValueError:
                print("Write number.")

    save_students(students)
    print("Student added.")


def show_students(students):
    return ", ".join(students.keys())


def show_student_grades(students):
    for student, subjects in students.items():
        # print(f"{student} - {subjects}")
        print()
        print(student)
        print()

        for subj, mark in subjects.items():
            print(subj ,end=" - ")
            for i in mark:
                print(i , end=", ")

            print()
        print()


def show_student_average(students):
    while True:
        average = 0
        average_del = 0

        print(f"Choose student {show_students(students)} or stop")
        name = input("> ").capitalize()

        if name not in students.keys() and name.lower() != "stop":
            print("Wrong name")

        elif name.lower()== "stop":
            break

        else:
            for subject, marks in students[name].items():
                print(f"{subject} average - {sum(marks)/len(marks)}")
                average_del += len(marks)
                average += sum(marks)

            average = average/average_del
            print(f"Average - {average}")

        print()


def show_subject_average(students):
    subjects_list = []
    all_marks = []

    for student, subjects in students.items():
        for subj in subjects.keys():
            subjects_list.append(subj)
    subjects_list = set(subjects_list)


    while True:
        for i in subjects_list:
            print(i)

        subjects_list = []
        all_marks = []

        print()
        print("write subject name or stop")
        subj_name = input("> ").lower()
        if subj_name == "stop":
            break

        else:
            if subj_name in subjects_list:
                for student in students:
                    if subj_name in students[student]:
                        all_marks.extend(students[student][subj_name])

                average = sum(all_marks)//len(all_marks)
                print(f"{subj_name} average - {average}")
                print()

            else:
                print("Subject not found")


def show_best_student(students):
    best_student = None
    best_average = 0

    for name in students.keys():
        average = 0
        average_del = 0

        for marks in students[name].values():
            average_del += len(marks)
            average += sum(marks)

        average = average/average_del

        if average > best_average:
            best_average = average
            best_student = name

    print(f"Best student is {best_student} - {best_average}")





def menu():
    students = load_students()

    while True:
        print("""
Student Grade Analyzer

1. Add student or grade
2. Show students
3. Show student grades
4. Show student average
5. Show subject average
6. Show best student
7. Exit
""")

        chooseDo= input("> ").lower()
        print()

        if chooseDo in ("add student", "add", "1", "add student or grade", "grade", "add grade"):
            add_student(students)
            print()

        elif chooseDo in ("show students", "2"):
            print(show_students(students))
            wait()

        elif chooseDo in ("show student grades","3"):
            show_student_grades(students)
            wait()

        elif chooseDo in ("show student average", "4"):
            show_student_average(students)
            wait()

        elif chooseDo in ("show subject average", "5"):
            show_subject_average(students)
            wait()

        elif chooseDo in ("show best student","6"):
            show_best_student(students)
            wait()

        elif chooseDo in ("exit", "7"):
            break
        else:
            print("Unknown command")


if __name__ == "__main__":
    menu()