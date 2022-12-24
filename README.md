# CIS-344
Explanation for mysql

This code creates a database and two tables in a MySQL system, and populates the tables with data.

First, the code creates a new database called "teachers_portal" using the "CREATE DATABASE" statement. It then selects the database for use using the "USE" statement.

Next, the code creates two tables called "students" and "courses" using the "CREATE TABLE" statement. The "students" table has columns for a student ID, student name, the ID of the course they are enrolled in, and their grade. The "courses" table has columns for a course ID and course name.

The code then inserts rows into the "students" table using the "INSERT INTO" statement. Each row represents a student, with values for their name, the ID of the course they are enrolled in, and their grade.

The code also inserts rows into the "courses" table using the "INSERT INTO" statement. Each row represents a course, with a value for the course name.

Finally, the code creates a stored procedure called "studentsWithGrade" using the "CREATE PROCEDURE" statement. A stored procedure is a predefined set of SQL statements that can be called by name. The stored procedure in this code selects data from both the "students" and "courses" tables, and returns the student name, course name, and grade for each student.


Explanation for Portaldatabase

This code defines a Python class called "Database" that can be used to connect to a MySQL database, execute SQL statements, and retrieve data from the database.

The class has several methods:

The __init__ method is the constructor for the class. It is called when an object of the class is created, and initializes the object's attributes with the given values. In this case, the attributes are the hostname, port number, database name, and login credentials for the database.

The connect method establishes a connection to the database using the mysql.connector library. It checks if the connection was successful, and prints an error message if it was not.

The getAllStudents method retrieves all students from the database by calling the "studentsWithGrade" stored procedure. It returns the results of the stored procedure as a list of records.

The addStudent method inserts a new student into the "students" table of the database. It takes three arguments: the student's name, the ID of the course they are enrolled in, and their grade
.


Explanation for PortalServer

This code defines a Python class called "PortalServer" that is used to create a web server for a teacher's portal application. The server is implemented using the HTTPServer and BaseHTTPRequestHandler classes from the http.server module.

The PortalServer class has several methods:

The do_POST method handles HTTP POST requests sent to the server. When the server receives a POST request, it sends a response with a status code of 200 (OK) and a header indicating that the response body contains HTML. It then processes the request based on the path specified in the request.
If the path is "/addStudent", the method retrieves form data from the request body using the cgi.FieldStorage class, and calls the addStudent method of a Database object to add a new student to the database. If the path is "/addCourse", the method retrieves form data from the request body and calls the addCourse method of the Database object to add a new course to the database.

The do_GET method handles HTTP GET requests sent to the server. When the server receives a GET request, it sends a response with a status code of 200 (OK) and a header indicating that the response body contains HTML. It then processes the request based on the path specified in the request.
If the path is "/", the method sends an HTML page with links to the other pages on the portal. If the path is "/addStudent", the method sends an HTML page with a form for adding a new student to the database. If the path is "/addCourse", the method sends an HTML page with a form for adding a new course to the database. If the path is "/searchStudent", the method sends an HTML page with a form for searching for a student by ID.

The send_page method is a helper method that sends an HTML page as the response to a request. It takes two arguments: a page title and the body of the page. It constructs an HTML page with the given title and body, and sends it to the client.

The send_form method is a helper method that sends an HTML form as the response to a request. It takes three arguments: a form action, a form method, and the body of the form. It constructs an HTML form with the given action, method, and body, and sends it to the client.

The send_message method is a helper method that sends an HTML page with a message as the response to a request. It takes two arguments: a message title and the message itself. It constructs an HTML page with the given title and message, and sends it to the client.

This code defines a function called run that starts an HTTP server using the HTTPServer class from the http.server module. The server listens for incoming HTTP requests on a specified port, and processes them using the PortalServer class.

The run function takes three arguments:

server_class: The class to use for the server. The default value is HTTPServer.
handler_class: The class to use for the request handler. The default value is PortalServer.
port: The port number to listen on. The default value is 8000.
The function creates an instance of the server_class class, passing it the server address (an empty string for the hostname and the specified port number) and the handler_class object as arguments. It then starts the server using the serve_forever method.

The run function also has a try-except block that catches IOError exceptions and sends an HTTP error response with a status code of 404 (Not Found) to the client. This is used to handle cases where the server receives a request for a file or resource that does not exist.

Finally, the run function is called at the end of the code to start the server.

