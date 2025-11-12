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
- Form submission handled via Flask routes

- Data stored persistently in MySQL

- Success/failure messages displayed on UI

### 3. 📊 Data Retrieval
- Route to view all registered students

- Data displayed in tabular format using HTML

### 4. ✨ Optional Enhancements
- Edit/Delete student records

- Styling with Bootstrap or custom CSS

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
![Student-Registration](https://github.com/user-attachments/assets/c6232e3c-8b26-4aef-b632-8e158f9423f1)

### Registered Students
![Registered-students](https://github.com/user-attachments/assets/3c790234-1e5e-4f01-ae31-1fdc849e33a0)

### 📋 Student List
![records-saved-in-DB](https://github.com/user-attachments/assets/22b1f3d6-9ba4-402c-b1a8-d85b49728d19)

## 🧠 Component Breakdown
| **Component**       | **Description**                                   |
|----------------------|---------------------------------------------------|
| `app.py`             | Main Flask application with routes                |
| `templates/`         | HTML templates for form and student list          |
| `static/`            | CSS and JS files                                  |
| `db.py`              | MySQL connection and query logic                  |
| `config.py`          | Configuration settings                            |
| `requirements.txt`   | Python dependencies                               |

## 🚀 Deployment (Optional)
- You can deploy this app using Jenkins and EC2:

- Install Jenkins on EC2

- Configure GitHub webhook for CI/CD

- Create Jenkins pipeline to pull code and restart Flask app

## 📬 Contact & Contribution
- Feel free to fork the repo and submit pull requests. For issues or suggestions, open a GitHub issue.

