# 🎓 Flask-Based Student Registration Web Application

## 📌 Objective

This project aims to develop and deploy a Flask-based web application that allows users to register students via a web form. The application stores submitted data in a MySQL database and provides functionality to retrieve and display student records. It serves as a hands-on learning experience in web development, backend integration, and deployment automation using Jenkins.

---

## 🧰 Technology Stack

- **Frontend**: HTML, CSS (Bootstrap optional)
- **Backend**: Python (Flask)
- **Database**: MySQL
- **Version Control**: Git & GitHub
- **Deployment**: Jenkins (Optional: EC2)

---

## 📁 GitHub Repository

🔗 [GitHub Repo](https://github.com/Prashanttmahamuni/Student-reg-flask-app.git)

> Fork or clone the repository to begin development:
```bash
git clone https://github.com/Prashanttmahamuni/Student-reg-flask-app.git
```
## 🧩 Functional Features
### 1. 📝 Student Registration Form
<span style="color: green;">●</span> Fields:
- Name
- Email
- Phone Number
- Course
- Address

<span style="color: green;">●</span> Input validation:
- Client-side (HTML5)
- Server-side (Flask)

### 2. 💾 Data Handling
<span style="color: green;">●</span> Form submission handled via Flask routes

<span style="color: green;">●</span> Data stored persistently in MySQL

<span style="color: green;">●</span> Success/failure messages displayed on UI

### 3. 📊 Data Retrieval
<span style="color: green;">●</span> Route to view all registered students

<span style="color: green;">●</span> Data displayed in tabular format using HTML

### 4. ✨ Optional Enhancements
<span style="color: green;">●</span> Edit/Delete student records

<span style="color: green;">●</span> Styling with Bootstrap or custom CSS

## ⚙️ Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/swati-zampal/stud-reg-flask-app.git
cd stud-reg-flask-app
```
### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure MySQL Database
- Create a database named student_db

- Update config.py or .env with your DB credentials:

```python
DB_HOST = 'localhost'
DB_USER = 'your_username'
DB_PASSWORD = 'your_password'
DB_NAME = 'student_db'
```
### 5. Run the Application
```bash
python app.py
Visit http://localhost:5000 in your browser.
```
## 🖼️ Screenshots
### 🧾 Registration Form

### 📋 Student List
