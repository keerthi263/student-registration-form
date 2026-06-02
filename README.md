# student-registration-form
# Student Registration CRUD App

## Overview

The Student Registration CRUD App is a full-stack web application that allows users to manage student records. The application provides functionality to create, read, update, and delete student information through a simple and user-friendly interface.

This project is built using:

* Frontend: Svelte
* Backend: Python Flask
* Database: SQLite
* API Communication: REST API

---

## Features

### Create Student

Users can add a new student by entering:

* Name
* Email
* Course

### Read Students

View all registered students in a table format.

### Update Student

Modify existing student details using the Edit button.

### Delete Student

Remove student records from the database using the Delete button.

### REST API Integration

The frontend communicates with the backend through RESTful API endpoints.

---

## Technology Stack

### Frontend

* Svelte
* HTML
* CSS
* JavaScript
* Vite

### Backend

* Python
* Flask
* Flask-CORS

### Database

* SQLite

---

## Project Structure

student-registration-app/

├── backend/

│ ├── app.py

│ └── students.db

│

├── frontend/

│ ├── src/

│ │ ├── App.svelte

│ │ └── main.js

│ ├── package.json

│ └── vite.config.js

│

└── README.md

---

## API Endpoints

### Get All Students

GET /students

Returns all student records.

### Add Student

POST /students

Request Body:

{
"name": "John",
"email": "[john@example.com](mailto:john@example.com)",
"course": "Computer Science"
}

### Update Student

PUT /students/{id}

Updates an existing student record.

### Delete Student

DELETE /students/{id}

Deletes a student record.

---

## Installation

### Backend Setup

1. Navigate to backend folder

cd backend

2. Install dependencies

pip install flask flask-cors


3. Run the Flask server

python app.py

Backend runs on:

http://127.0.0.1:5000

### Frontend Setup

1. Navigate to frontend folder
2. 
cd frontend

3. Install dependencies

npm install

3. Start the development server

npm run dev

Frontend runs on:

http://localhost:5173

## Learning Outcomes

Through this project, I learned:

* Building REST APIs using Flask
* CRUD operations with SQLite
* Connecting frontend and backend applications
* Handling HTTP requests and responses
* Using Svelte for reactive user interfaces
* Cross-Origin Resource Sharing (CORS)
* Full-stack application development

-
