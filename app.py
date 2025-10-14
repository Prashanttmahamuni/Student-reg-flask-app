from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",
    database="student_db"
)
cursor = conn.cursor()

# Home page with registration form
@app.route('/')
def index():
    return render_template('index.html')

# Handle form submission
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    course = request.form['course']
    address = request.form['address']

    cursor.execute("INSERT INTO students (name, email, phone, course, address) VALUES (%s, %s, %s, %s, %s)",
                   (name, email, phone, course, address))
    conn.commit()
    return redirect('/students')

# Display all students
@app.route('/students')
def students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    return render_template('students.html', students=data)

# Delete a student
@app.route('/delete/<int:id>')
def delete_student(id):
    cursor.execute("DELETE FROM students WHERE id = %s", (id,))
    conn.commit()
    return redirect('/students')

# Show edit form
@app.route('/edit/<int:id>')
def edit_student(id):
    cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
    student = cursor.fetchone()
    return render_template('edit.html', student=student)

# Handle update
@app.route('/update/<int:id>', methods=['POST'])
def update_student(id):
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    course = request.form['course']
    address = request.form['address']

    cursor.execute("""
        UPDATE students SET name=%s, email=%s, phone=%s, course=%s, address=%s WHERE id=%s
    """, (name, email, phone, course, address, id))
    conn.commit()
    return redirect('/students')

if __name__ == '__main__':
    app.run(debug=True)
