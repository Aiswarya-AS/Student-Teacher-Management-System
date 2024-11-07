from student_functions import view_students, add_student, update_user, delete_user
from teacher_functions import get_teachers_db, get_teachers
from common_functions import register_user, login, map_student_teacher
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/view_students', methods=['GET'])
def get_students_api():
    students = view_students()
    return jsonify(students)


@app.route('/register', methods=['POST'])
def register_api():
    data = request.json
    user_type = data.get("user_type")
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    db_name = data.get("db_name", "student_management")

    try:
        register_user(user_type, name, email, password, db_name)
        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/login', methods=['POST'])
def login_api():
    data = request.json
    user_type = data.get("user_type")
    email = data.get("email")
    password = data.get("password")
    db_name = data.get("db_name", "student_management")

    try:
        login(user_type, email, password, db_name)
        return jsonify({"message": "User logged in Succesfully!!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/add_student', methods=['POST'])
def add_student_api():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    try:
        add_student(name, email, password)
        return jsonify({"message": "User Created sucessfully!!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/update_student', methods=['PUT'])
def update_student_api():
    data = request.json
    student_id = data.get("student_id")
    name = data.get("name")
    email = data.get("email")

    try:
        update_user(student_id, name, email)
        return jsonify({"message": "User updated sucessfully!!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/delete_student', methods=['DELETE'])
def delete_student_api():
    data = request.json
    student_id = data.get("student_id")

    try:
        delete_user(student_id)
        return jsonify({"message": "User deleted!!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_teachers/<int:id>', methods=['GET'])
def get_teachers_two_db(id):
    try:
        teachers = get_teachers(id)
        return jsonify(teachers)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_teachers_same_db/<int:id>', methods=['GET'])
def get_teachers_same_db(id):
    try:
        teachers = get_teachers_db(id)
        return jsonify(teachers)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/map_users', methods=['POST'])
def map_users():
    data = request.json
    student_id = data.get("student_id")
    teacher_id = data.get("teacher_id")

    try:
        map_student_teacher(student_id, teacher_id)
        return jsonify({"message": "Mapping Successfull"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
