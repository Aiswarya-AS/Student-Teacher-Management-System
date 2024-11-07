from db_connection import connect_to_db, close_connection


def view_students():
    """
    Displays a list of all students.
    """
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    close_connection(conn, cur)
    return rows


def add_student(name, email, password):
    """
    Adds a new student to the database.
    """
    from utils import hash_password  
    hashed_password = hash_password(password)
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, email, password) VALUES (%s, %s, %s)",
                (name, email, hashed_password))
    conn.commit()
    close_connection(conn, cur)


def update_user(student_id, name, email):
    """Updates an existing student in db."""
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("UPDATE students SET name = %s, email = %s WHERE id = %s",
                (name, email, student_id))
    conn.commit()
    close_connection(conn, cur)


def delete_user(student_id):
    """Deletes a student from the db."""
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    close_connection(conn, cur)
