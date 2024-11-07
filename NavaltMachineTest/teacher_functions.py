from db_connection import connect_to_db, close_connection


def get_teachers(student_id):
    """
    When diffrent databses
    """
    conn = connect_to_db()
    cur = conn.cursor()
    try:
        create_extension_query = "CREATE EXTENSION IF NOT EXISTS dblink;"
        cur.execute(create_extension_query)
        # Define the dblink query to join the tables
        dblink_query = """
            SELECT s.id AS student_id, s.name AS student_name, t.name AS teacher_name
            FROM students AS s
            JOIN student_teacher AS st ON s.id = st.student_id
            JOIN dblink('dbname=teacher_management user=postgres password=123',
                        'SELECT id, name FROM teachers') 
            AS t(id INTEGER, name TEXT) 
            ON st.teacher_id = t.id;
        """
        cur.execute(dblink_query)

        results = cur.fetchall()
        teachers = []
        for row in results:
            if row[0] == student_id:
                teachers.append(row[2])
                print(f"Student ID: {row[0]}, Student Name: {row[1]}, Teacher Name: {row[2]}")
        return teachers
    except Exception as e:
        print(e)
    finally:
        close_connection(conn, cur)


def get_teachers_db(student_id):
    """
    when the two tables are in same db
    """
    conn = connect_to_db()
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT t.name 
            FROM student_teacher st
            JOIN teachers t ON st.teacher_id = t.id
            WHERE st.student_id = %s
        """, (student_id,))

        teachers = cur.fetchall()

        teacher_names = [teacher[0] for teacher in teachers]
        print(teacher_names)
        return teacher_names

    except Exception as e:
        print(f"Error fetching teachers: {e}")
        return []

    finally:
        close_connection(conn, cur)
