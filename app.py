from flask import Flask,render_template,request
from db import db,cursor
app=Flask(__name__)
@app.route('/')
def home():
	return render_template('index.html')
@app.route('/add',methods=['GET','POST'])
def add_employee():
    if request.method=='POST':
        name=request.form['name']
        department=request.form['department']
        salary=request.form['salary']  
        query = """
        INSERT INTO employees(name, department, salary)
        VALUES(%s, %s, %s)
    	"""
        values = (name, department, salary)
        cursor.execute(query, values)
        db.commit()
        return "Employee Added Successfully"
    return render_template('add.html')
@app.route('/view')
def view_employee():
    query="Select * FROM employees"
    cursor.execute(query)
    data=cursor.fetchall()
    return render_template('view.html',employees=data)
@app.route('/update', methods=['GET', 'POST'])
def update_employee():

    if request.method == 'POST':

        e_id = request.form['id']
        salary = request.form['salary']

        query = """
        UPDATE employees
        SET salary=%s
        WHERE e_id=%s
        """

        values = (salary, e_id)

        cursor.execute(query, values)

        db.commit()

        return "Employee Updated Successfully"

    return render_template('update.html')	
@app.route('/delete',methods=['GET','POST'])
def delete_employee():
    if request.method=='POST':
        e_id=request.form['id']
        query="DELETE FROM employees WHERE e_id=%s"
        values=(e_id,)
        cursor.execute(query,values)
        db.commit()
        return "employee deleted"
    return render_template('delete.html')
if __name__=='__main__':
	app.run(debug=True)
