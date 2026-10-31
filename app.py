
students = []

def add_student(roll_no, name, marks):
    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks
    }
    students.append(student)
    return "Student added successfully"

def view_students():
    return students

def search_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return student
    return None

def delete_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            return "Student deleted successfully"
    return "Student not found"

if __name__ == "__main__":
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            roll = int(input("Enter roll number: "))
            name = input("Enter name: ")
            marks = float(input("Enter marks: "))
            print(add_student(roll, name, marks))

        elif choice == "2":
            print(view_students())

        elif choice == "3":
            roll = int(input("Enter roll number: "))
            print(search_student(roll))

        elif choice == "4":
            roll = int(input("Enter roll number: "))
            print(delete_student(roll))

        elif choice == "5":
            break

        else:
            print("Invalid choice")
