# Employee Attendance Tracker
This is a lightweight Employee Management API built with FastAPI and SQlite. It provides basic CRUD(create, read, update, delete) operations for managing employee records.

Endpoints:
⦁	GET/employees/{emp_id}: Retrieve employee details by ID.
⦁	POST/employees/: Add a new employee
⦁	PUT/employees/{emp_id}: Update an existing employee.
⦁	DELETE/employees/{emp_id}: Delete an employee.

Error Handling:
The API handles errors such as 404(Not found) and 400(Bad Request) when invalid data is provided.

Run the Dockerfile:
⦁	Go to the folder containing Dockerfile and the source code then try the command: docker build -attendancetracker .
⦁	Once the image is built, you can run a Docker container based on that image using the command: docker run -p 8000:8000 attendancetracker.
⦁	access the app from the Swagger UI using the URL http://localhost:8000/docs
