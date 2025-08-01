student_data = {}

def add_new_student(name, grades):
    if (name not in student_data) and name and grades:
        if check_grades(grades):
            student_data[name] = list(grades)
            return f"Student {name} successfully added.\n"
        else:
            return "One of the grade values is out of range"
    else:
        return "Please make sure both name and grades are provided\n"
    
def add_grade(student, grade):
    if student in student_data and grade > -1 and grade < 101:
        student_data[student].append(grade)
        return f"{student}'s grade added: {student_data[student]}\n"
    else:
        return "Please make sure student is registered and grade is between 0 and 100 inclusive\n"
    
def view_student_average_and_letter_grade(student):
    if student in student_data:
        student_average = calculate_average(student)
        letter_grade = ""

        if student_average > 89:
            letter_grade = 'A'
        elif student_average > 79:
            letter_grade = 'B'
        elif student_average > 69:
            letter_grade = 'C'
        elif student_average > 59:
            letter_grade = 'D'
        else:
            letter_grade = 'F'

        return f"{student}'s Average: {student_average} (Grade {letter_grade})\nGrades: {student_data[student]}\n"
    else:
        return f"Student {student} doesn't exist\n"


def class_average():
    sum_total = 0
    key_list = list(student_data.keys())
    for student in key_list:
        sum_total += calculate_average(student)

    return sum_total / key_list


def rank():
    high_avrg = 0
    low_avrg = 0
    highest = ""
    lowest = ""
    key_list = list(student_data.keys())

    for student in key_list:
        if calculate_average(student) > high_avrg:
            highest = student
        if calculate_average(student) < low_avrg:
            lowest = student

    return f"Class Average: {class_average()}\nHighest: {highest}, Highest Average: {high_avrg}\nLowest: {lowest}, Lowest Average: {low_avrg}\n "


def calculate_average(student):
    if student in student_data:
        grades = student_data[student]
        return sum(grades) / len(grades)

def check_grades(grades):
    for grade in grades:
        if grade < 0 or grade > 101:
            return False
    return True

# entry point to student gradebook
def entry():
    print("\n=== STUDENT GRADEBOOK MANAGER ===\n")

    while True:
        choice = input("1. Add Student\n2. Add Grade\n3. View Student Report\n4. Class Statistics\n5. Exit\n\nChoice:  ")
        if choice == "1":
            student = input("Enter name: ")
            grades = []
            while True:
                grade = float(input("Enter grade(enter -1 to stop): "))
                if grade != -1:
                    grades.append(grade)
                else:
                    break
            print(add_new_student(student, grades))

        elif choice == "2":
            student = input("Enter student: ")
            grade = float(input("Enter grade: "))
            print(add_grade(student, grade))
        
        elif choice == "3":
            student = input("Enter name: ")
            print(view_student_average_and_letter_grade(student))

        elif choice == "4":
            print(f"Class statistics: \n{rank()}")

        elif choice == "5":
            print("Closing system......")
            break
        else:
            print("Invalid input!\nAborting....!")
            break


entry()