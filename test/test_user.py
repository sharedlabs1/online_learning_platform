import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from user import User, Student, Instructor
import unittest

class TestUserSystem(unittest.TestCase):

    def test_user_creation(self):
        # Test User class initialization with valid inputs
        u = User("Alice", "alice@example.com")
        self.assertEqual(u.name, "Alice")
        self.assertEqual(u.email, "alice@example.com")

    def test_student_inherits_user(self):
        # Test Student class inheritance and initialization
        s = Student("Bob", "bob@example.com")
        self.assertIsInstance(s, User)
        self.assertEqual(s.name, "Bob")
        self.assertEqual(s.email, "bob@example.com")

    def test_enroll_course(self):
        # Test enrolling a course for a student
        s = Student("Carol", "carol@example.com")
        s.enroll("Python")
        self.assertIn("Python", s.course_list)

    def test_instructor_inherits_user(self):
        # Test Instructor class inheritance and initialization
        i = Instructor("Dan", "dan@example.com")
        self.assertIsInstance(i, User)
        self.assertEqual(i.name, "Dan")
        self.assertEqual(i.email, "dan@example.com")

    def test_assign_course(self):
        # Test assigning a course to an instructor
        i = Instructor("Eve", "eve@example.com")
        i.assign_course("Data Science")
        self.assertIn("Data Science", i.courses_teaching)

if __name__ == "__main__":
    unittest.main()
