
import unittest

from app import (
    add_student,
    view_students,
    search_student,
    delete_student,
    students
)


class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        students.clear()

    def test_add_student(self):
        result = add_student(1, "Ravi", 85)
        self.assertEqual(result, "Student added successfully")

    def test_view_students(self):
        add_student(1, "Ravi", 85)
        self.assertEqual(len(view_students()), 1)

    def test_search_student(self):
        add_student(1, "Ravi", 85)
        result = search_student(1)
        self.assertEqual(result["name"], "Ravi")

    def test_delete_student(self):
        add_student(1, "Ravi", 85)
        result = delete_student(1)
        self.assertEqual(result, "Student deleted successfully")

    def test_invalid_marks(self):
        with self.assertRaises(ValueError):
            add_student(2, "Sita", 150)


if __name__ == "__main__":
    unittest.main()
