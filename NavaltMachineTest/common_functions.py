from db_connection import connect_to_db, close_connection
from utils import hash_password


def register_user(user_type, name, email, password, db_name="student_management"):
    """
    Registers a new user (student or teacher).
    """
    hashed_password = hash_password(password)
    conn = connect_to_db(db_name)
    cur = conn.cursor()

    if user_type == "student":
        cur.execute("INSERT INTO students (name, email, password) VALUES (%s, %s, %s)",
                    (name, email, hashed_password))
    elif user_type == "teacher":
        cur.execute("INSERT INTO teachers (name, email, password) VALUES (%s, %s, %s)",
                    (name, email, hashed_password))

    conn.commit()
    close_connection(conn, cur)


def login(user_type, email, password, db_name="student_management"):
    """
    Attempts to login a user and logs the attempt.
    """
    from db_connection import connect_to_db, close_connection
    hashed_password = hash_password(password)

    conn = connect_to_db(db_name)
    cur = conn.cursor()
    if user_type == "student":
        cur.execute(
            "SELECT id FROM students WHERE email = %s AND password = %s", (email, hashed_password))
    elif user_type == "teacher":
        cur.execute(
            "SELECT id FROM teachers WHERE email = %s AND password = %s", (email, hashed_password))

    user_id = cur.fetchone()

    if user_id:
        # Log the login attempt
        cur.execute("INSERT INTO logs (user_type, user_id, login_time, database_name) VALUES (%s, %s, NOW(), %s)",
                    (user_type, user_id[0], db_name))
        conn.commit()
        print("Login successful!")
    else:
        print("Invalid credentials")

    close_connection(conn, cur)


def map_student_teacher(student_id, teacher_id):
    """
    Map student with teacher

    """
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO student_teacher (student_id, teacher_id) VALUES (%s, %s)",
                (student_id, teacher_id))
    conn.commit()
    close_connection(conn, cur)
