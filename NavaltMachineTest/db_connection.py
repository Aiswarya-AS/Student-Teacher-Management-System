import psycopg2


# Your database default is student_management
def connect_to_db(db="student_management"):
    """
    Connects to the specified database.
    """
    conn = psycopg2.connect(
        database=db,
        user="postgres",  # User
        password="",  # postgres password
        host="localhost"
    )
    return conn


def close_connection(conn, cur):
    """
    Closes the database connection and cursor.
    """
    cur.close()
    conn.close()
