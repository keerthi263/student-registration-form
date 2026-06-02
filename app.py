from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = 'students.db'


def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            course TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


init_db()


@app.route('/students', methods=['GET'])
def get_students():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()

    students = []

    for row in rows:
        students.append({
            'id': row[0],
            'name': row[1],
            'email': row[2],
            'course': row[3]
        })

    conn.close()

    return jsonify(students)


@app.route('/students', methods=['POST'])
def add_student():
    data = request.json

    name = data['name']
    email = data['email']
    course = data['course']

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO students (name, email, course) VALUES (?, ?, ?)',
        (name, email, course)
    )

    conn.commit()
    conn.close()

    return jsonify({'message': 'Student added successfully'})


@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json

    name = data['name']
    email = data['email']
    course = data['course']

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        'UPDATE students SET name=?, email=?, course=? WHERE id=?',
        (name, email, course, id)
    )

    conn.commit()
    conn.close()

    return jsonify({'message': 'Student updated successfully'})


@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM students WHERE id=?', (id,))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Student deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
