class User:
    def __init__(self, name, email):
        # Initialize name and email attributes
        self.name = name
        self.email = email

class Student(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.course_list = []

    def enroll(self, course_name):
        # Add the course to the course_list
        self.course_list.append(course_name)

class Instructor(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.courses_teaching = []

    def assign_course(self, course_name):
        # Add the course to the courses_teaching list
        self.courses_teaching.append(course_name)

def main():
    # Create a student and enroll in courses
    student = Student("Alice", "alice@example.com")
    student.enroll("Math 101")
    student.enroll("History 201")
    print(f"Student: {student.name}, Email: {student.email}, Enrolled Courses: {student.course_list}")

    # Create an instructor and assign courses
    instructor = Instructor("Bob", "bob@example.com")
    instructor.assign_course("Math 101")
    instructor.assign_course("Physics 301")
    print(f"Instructor: {instructor.name}, Email: {instructor.email}, Courses Teaching: {instructor.courses_teaching}")

if __name__ == "__main__":
    main()
