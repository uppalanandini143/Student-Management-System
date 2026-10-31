
students = []


# Add Student
def add_student(roll_no, name, marks):
    if not isinstance(marks, (int, float)) or isinstance(marks, bool):
        raise ValueError("Marks must be a number")

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks
    }

    students.append(student)
    return "Student added successfully"


# View Students
def view_students():
    return students


# Search Student
def search_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return student
    return None


# Delete Student
def delete_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            return "Student deleted successfully"

    return "Student not found"


# Main Program
if __name__ == "__main__":

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            roll_no = int(input("Enter roll number: "))
            name = input("Enter student name: ")
            marks = float(input("Enter marks: "))

            try:
                print(add_student(roll_no, name, marks))
            except ValueError as error:
                print(error)

        elif choice == "2":
            print(view_students())

        elif choice == "3":
            roll_no = int(input("Enter roll number: "))
            print(search_student(roll_no))

        elif choice == "4":
            roll_no = int(input("Enter roll number: "))
            print(delete_student(roll_no))

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")
