from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

def connect_database():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees (
              id TEXT PRIMARY KEY, 
              name TEXT, 
              status TEXT
    )''')
    conn.commit()
    return conn

@app.get("/employees/{emp_id}")
def get_employee(emp_id: str):
    conn = connect_database()
    c = conn.cursor()
    c.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
    emp_details = c.fetchone()
    conn.close()
    if emp_details is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"id": emp_details[0], "name": emp_details[1], "status": emp_details[2]}

@app.post("/employees/")
def add_employee(emp_id: str, name: str, status: str = "absent"):
    if status not in ["present", "absent"]:
        raise HTTPException(status_code=400, detail = "Invalid status, must be present or absent.")
    
    conn = connect_database()
    c = conn.cursor()
    c.execute("SELECT * FROM employees where id=?", (emp_id,))
    if c.fetchone():
        raise HTTPException(status_code=400, detail="Employee already exists")
    c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_id, name, status))
    conn.commit()
    conn.close()
    return {"message": "Employee added successfully"}

@app.put("/employees/{emp_id}")
def update_employee(emp_id: str, name: str, status: str):
    if status not in ["present", "absent"]:
        raise HTTPException(status_code=400, detail = "Invalid status, must be present or absent")
    
    conn = connect_database()
    c = conn.cursor()
    c.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
    emp_details = c.fetchone()
    if emp_details is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    c.execute("UPDATE employees SET name=? WHERE id=?", (name, status, emp_id))
    conn.commit()
    conn.close()
    return {"message": "Employee updated successfully"}

@app.delete("/employees/{emp_id}")
def delete_employees(emp_id: str):
    conn = connect_database()
    c =  conn.cursor()
    c.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
    if c.fetchone() is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    c.execute("DELETE FROM employees WHERE id=?", (emp_id,))
    conn.commit()
    conn.close()
    return {"message": "Employee deleted successfully"}





#def update_employee(conn):
 #   c = conn.cursor()
  #  emp_id = input("Enter employee ID: ")
   # c.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
    #emp_details = c.fetchone()
    #if emp_details is None:
     #   print("Employee not found!")
      #  return
    #emp_name = input("Enter updated name: ")
    #c.execute("UPDATE employees SET name=? WHERE id=?", (emp_name, emp_id))
    #conn.commit()
    #print("Employee updated successfully!")

#def delete_employee(conn):
 #   c = conn.cursor()
#    emp_id = input("Enter employee ID: ")
 #   c.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
 #   if c.fetchone() is None:
  #      print("Employee not found!")
   #     return
   # c.execute("DELETE FROM employees WHERE id=?", (emp_id,))
   # conn.commit()
    #print("Employee deleted successfully!")

