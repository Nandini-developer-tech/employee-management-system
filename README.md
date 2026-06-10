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
## Project Screenshots

### Home Page

<img width="1912" height="887" alt="image" src="https://github.com/user-attachments/assets/a6efbdc8-a133-4c05-84e2-3fe24b55f7f0" />


The home page provides an overview of the Employee Management System and contains a navigation bar for accessing CRUD operations.      

---

### Add Employee Page

<img width="1912" height="857" alt="image" src="https://github.com/user-attachments/assets/2133d16f-42d0-40d5-91d9-edecca170432" />


This page allows users to add a new employee by entering employee details such as name, department, and salary.     

---

### View Employee Page     

<img width="1907" height="872" alt="image" src="https://github.com/user-attachments/assets/eae69613-3c09-4757-9970-4e18c3762f14" />


This page displays all employee records stored in the MySQL database in a tabular format.

---

### Update Employee Page

<img width="1907" height="862" alt="image" src="https://github.com/user-attachments/assets/169b3047-b898-4109-8d1d-8accd554b8a8" />


This page allows users to update employee information by providing the Employee ID and new salary.
    
---

### Delete Employee Page

<img width="1912" height="868" alt="image" src="https://github.com/user-attachments/assets/bcbdac83-828a-44a8-a217-479adbe51dff" />


This page allows users to remove employee records from the database using the Employee ID.

---

### Database Table (Optional)

<img width="1467" height="777" alt="image" src="https://github.com/user-attachments/assets/bb5de10a-44c8-4574-91ca-b4728d797e4e" />




This screenshot shows the employee records stored in the MySQL database.


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
