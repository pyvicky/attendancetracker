import sqlite3

def connect_database():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees (
              id TEXT PRIMARY KEY, 
              name TEXT, 
              status TEXT
    )''')
    conn.commit
    return conn


def mark_attendance(conn):
    c = conn.cursor()
    emp_id = input("Enter employee ID: ")
    c.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
    emp_details = c.fetchone()
    if emp_details is None:
        print("Employee not found!")
        return
    emp_name = emp_details[1]
    attendance = input(f"Is {emp_name} present? (P/A): ").upper()
    while attendance not in ['P', 'A']:
        print("Please enter a valid input, P for Present and A for absent")
        attendance = input(f"Is {emp_name} present? (P/A): ").upper()
    c.execute("UPDATE employees SET status=? WHERE id=?", (attendance, emp_id))
    conn.commit()
    print("Attendance marked successfully!")


def view_attendance(conn):
    c = conn.cursor()
    print("Attendance Report: ")
    c.execute("SELECT * FROM employees")
    for row in c.fetchall():
        print(f"{row[0]}: {row[2]}")
    print()

def list_employees(conn):
    c =  conn.cursor()
    print("List of Employees: ")
    c.execute("SELECT * FROM employees")
    for row in c.fetchall():
        print(f"{row[0]}: {row[1]}")



def add_employee(conn):
    c = conn.cursor()
    emp_id = input("Enter employee ID: ")
    c.execute("SELECT * FROM employees where id=?", (emp_id,))
    if c.fetchone():
        print("Employee already exists!")
        return
    emp_name = input("Enter employee name: ")
    c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_id, emp_name, "Absent"))
    conn.commit()
    print("Employee added successfully!")


def main():
    conn = connect_database()
    while True:
        print("1. Mark Attendance")
        print("2. View attendance report")
        print("3. List Employees")
        print("4. Add Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            mark_attendance(conn)
        elif choice == '2':
            view_attendance(conn)
        elif choice == '3':
            list_employees(conn)
        elif choice == '4':
            add_employee(conn)
        elif choice == '5':
            print("Bye!")
            conn.close()
            break

        else:
            print("Invalid choice, please enter a valid number")

if __name__ == "__main__":
    main()