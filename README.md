# 🧪 OOPs Case-Based Assignment: Online Learning Platform

## 📚 Objective

This assignment will test your understanding of:
- Creating Classes
- Using Constructors
- Implementing Inheritance

## 📁 Folder Structure

- `src/user.py` → Your code goes here
- `test/test_user.py` → Do not modify; used to test your implementation
- `solution/user_solution.py` → Instructor reference (you may ignore this)

## 🚀 Problem Statement

Create a basic object-oriented structure for an online learning platform:

1. `User`: A base class with `name` and `email`.
2. `Student`: Inherits from `User`. Adds `course_list` and an `enroll()` method.
3. `Instructor`: Inherits from `User`. Adds `courses_teaching` and an `assign_course()` method.

## ✅ Task Instructions

- Open `src/user.py`.
- Complete the `User`, `Student`, and `Instructor` classes.
- Run the tests with:

## Launch Tests from the Command Line

```bash
python -m unittest -v test_user
```

python3 -m unittest test/test_user.py
```

- You should pass all 5 tests.

## 💡 Notes

- Use `super().__init__(...)` to inherit from the base class.
- Append courses to lists in the appropriate methods.

## Constraints for User, Student, and Instructor Classes

To ensure proper functionality and pass all test cases, please adhere to the following constraints:

1. **User Class**:
   - `name` and `email` must be non-empty strings.
   - If invalid values are provided, raise a `ValueError` with an appropriate message.

2. **Student Class**:
   - Inherits from the `User` class.
   - `enroll(course_name)`:
     - `course_name` must be a non-empty string.
     - A student cannot enroll in the same course more than once. If attempted, raise a `ValueError`.

3. **Instructor Class**:
   - Inherits from the `User` class.
   - `assign_course(course_name)`:
     - `course_name` must be a non-empty string.
     - An instructor cannot be assigned to the same course more than once. If attempted, raise a `ValueError`.

4. **General Guidelines**:
   - Use proper error handling to validate inputs.
   - Ensure that all attributes are initialized correctly.
   - Avoid hardcoding values; use dynamic inputs where applicable.

## 🧪 Manual Test Data and Expected Output

Below are some sample inputs and their expected outputs to help you manually test your implementation:

### 1. User Class
#### Input:
```python
u = User("Alice", "alice@example.com")
print(u.name)
print(u.email)
```
#### Expected Output:
```
Alice
alice@example.com
```

---

### 2. Student Class
#### Input:
```python
s = Student("Bob", "bob@example.com")
s.enroll("Math 101")
s.enroll("History 201")
print(s.name)
print(s.email)
print(s.course_list)
```
#### Expected Output:
```
Bob
bob@example.com
['Math 101', 'History 201']
```

---

### 3. Instructor Class
#### Input:
```python
i = Instructor("Eve", "eve@example.com")
i.assign_course("Physics 301")
i.assign_course("Data Science")
print(i.name)
print(i.email)
print(i.courses_teaching)
```
#### Expected Output:
```
Eve
eve@example.com
['Physics 301', 'Data Science']
```

---

### 4. Combined Example
#### Input:
```python
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
```
#### Expected Output:
```
Student: Alice, Email: alice@example.com, Enrolled Courses: ['Math 101', 'History 201']
Instructor: Bob, Email: bob@example.com, Courses Teaching: ['Math 101', 'Physics 301']
```

---

### Notes:
- Use these examples to manually test your implementation in a Python shell or script.
- These examples align with the test cases provided in `test/test_user.py`.
