
# Student and Teacher Management System

This project is a Python-based management system for handling student and teacher information across two databases: `student_management` and `teacher_management`. It allows the management of student and teacher records, user registration, authentication, and linking teachers to students across databases with `dblink`.

There have been a lack of clarity in the intented output whether creating a single database or two databases each for student and teacher,  if you prefer single database just create `student_management` .


Postman Api collection file MachineTest-Navalt.postman_api_collection is also attached.

## Features
- **User Registration and Login**: Register and for `student` and `teacher` users.
- **CRUD Operations**: Add, update, view, and delete student records.
- **Cross-Database Queries**: Retrieve information about students' assigned teachers, even across separate databases using PostgreSQL `dblink`.
- **Logging**: Records login attempts with timestamped log entries.

## Installation

### Prerequisites
- **Python 3.x**
- **PostgreSQL** with `dblink` extension enabled.
- **Poetry** for dependency management.

### Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/Aiswarya-AS/Student-Teacher-Management-System.git
    cd student-teacher-management
    ```

2. Install dependencies using Poetry:
    ```bash
    poetry install
    ```

3. Set up PostgreSQL databases:
    - Create two PostgreSQL databases(two tables in different databases):
        - `student_management` for student information
        - `teacher_management` for teacher information
    - Create PostgreSQL databases(Only one database, 2 tables: students and teachers):
        - `student_management` for student and teacher information
        


4. Update the PostgreSQL connection details in the Python code (e.g., username, password).

## Database Setup

Create tables in each database as follows:
If you only want one database create `student_management` and tables `students` , `teachers`, `student_management`, `logs`, `student_teacher` tables.

### `student_management` Database

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(256)
);

CREATE TABLE student_teacher (
    student_id INTEGER REFERENCES students(id),
    teacher_id INTEGER
);
```

### `teacher_management` Database

```sql
CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(256)
);

--make sure to add logs in both if you are prefering two databases.

CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    user_type VARCHAR(50),
    user_id INTEGER,
    login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    database_name VARCHAR(100)
);
```

## Usage

### Functions

The project contains several utility functions:

- **`add_user(name, email, password)`**: Adds a new student.
- **`view_users()`**: Lists all students.
- **`update_user(student_id, name, email)`**: Updates a student's information.
- **`delete_user(student_id)`**: Deletes a student.
- **`register_user(user_type, name, email, password)`**: Registers a new user (student or teacher).
- **`login(user_type, email, password)`**: Authenticates a user and logs their login attempt.
- **`map_student_teacher(student_id, teacher_id)`**: Creates many to many realtionship between student and teacher.
- **`get_teachers(student_id)`**: Fetches teachers for a student using `dblink` across databases.
- **`get_teachers_db(student_id)`**: Fetches teachers when both tables are in the same database.

### To run code

```python

cd NavaltMachineTest

python main.py

```



