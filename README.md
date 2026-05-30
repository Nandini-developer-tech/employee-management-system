# Employee Management System

## Project Overview

The Employee Management System is a web application developed using Flask and MySQL. It allows users to manage employee records by performing CRUD (Create, Read, Update, Delete) operations through a simple and user-friendly interface.

## Features

* Add Employee
* View Employee Records
* Update Employee Information
* Delete Employee Records
* Navigation Bar for Easy Access
* MySQL Database Integration
* Responsive and Simple User Interface

---

## Technologies Used

### Backend

* Python
* Flask

### Database

* MySQL

### Frontend

* HTML
* CSS

---

## Project Structure

```
employee_management_system/
│
├── app.py
├── db.py
├── README.md
│
├── templates/
│   ├── index.html
│   ├── add.html
│   ├── view.html
│   ├── update.html
│   └── delete.html
│
└── static/
    └── (optional CSS files)
```

---

## Database Setup

### Create Database

```sql
CREATE DATABASE employee_db;
```

### Use Database

```sql
USE employee_db;
```

### Create Table

```sql
CREATE TABLE employees(
    e_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    department VARCHAR(100),
    salary INT
);
```

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
```

### Install Required Packages

```bash
pip install flask
pip install mysql-connector-python
```

---

## Database Connection

Update the database credentials in `db.py`.

```python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="employee_db"
)

cursor = db.cursor()
```

---

## Running the Application

```bash
python app.py
```

Open the browser and visit:

```
http://127.0.0.1:5000
```

---

## Application Routes

| Route   | Description     |
| ------- | --------------- |
| /       | Home Page       |
| /add    | Add Employee    |
| /view   | View Employees  |
| /update | Update Employee |
| /delete | Delete Employee |

---

## CRUD Operations

### Create

Adds a new employee record to the database.

### Read

Displays all employee records in a table format.

### Update

Updates employee salary using Employee ID.

### Delete

Deletes an employee record using Employee ID.

---

## Frontend Components

### Home Page

Displays project information and navigation menu.

### Add Employee Page

Contains a form to add employee details.

### View Employee Page

Displays employee records in a table.

### Update Employee Page

Allows updating employee salary.

### Delete Employee Page

Allows deleting an employee record.

---

## Future Enhancements

* Employee Search
* Employee Login System
* Bootstrap Styling
* Form Validation
* Responsive Design
* REST API Integration
* Deployment to Cloud Platforms

---

## Learning Outcomes

Through this project, the following concepts were learned:

* Flask Routing
* HTML Forms
* CSS Styling
* MySQL Integration
* CRUD Operations
* Database Connectivity
* Frontend and Backend Integration

---

## Author

Nandini

### Role

Python Backend Developer
