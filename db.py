import mysql.connector
db=mysql.connector.connect(
	host="localhost",
	user="root",
	password="tiger",
	database="employee_db"
)
cursor=db.cursor()