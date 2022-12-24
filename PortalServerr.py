import cgi
from http.server import HTTPServer, BaseHTTPRequestHandler
from portalDatabase import Database
class PortalServer(BaseHTTPRequestHandler):

    def __init__(self, *args):
        self.database = Database()
        BaseHTTPRequestHandler.__init__(self, *args)

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        try:
            if self.path == '/addStudent':
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                student_name = form.getvalue("sname")
                student_courseid = int(form.getvalue("courseid"))
                student_grade = float(form.getvalue("sgrade"))
                self.database.addStudent(student_name, str(student_courseid), str(student_grade))
                # Call the Database Method to add a new student
                '''
                    Example call: self.database.addStudent(student_name, student_courseid,student_grade)
                '''

                print("grabbed values", student_name, student_courseid, student_grade)

                self.wfile.write(b"<html><head><title> Teacher's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Teacher's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addStudent'>Add Student</a>|\
                                  <a href='/addCourse'>Add Course</a>|\
                                  <a href='/searchStudent'>Search Student By ID </a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Student have been added</h3>")
                self.wfile.write(b"<div><a href='/addStudent'>Add A New Student</a></div>")
                self.wfile.write(b"</center></body></html>")

            if self.path == '/addCourse':
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                # Retrieve the course name from the form
                course_name = form.getvalue("cname")

                # Add the course to the database
                next_id = self.database.addCourse(course_name)

                # Code to handle form submission goes here
                self.wfile.write(b"<html><head><title> Teacher's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Teacher's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                     <a href='/addStudent'>Add Student</a>|\
                                     <a href='/addCourse'>Add Course</a>|\
                                     <a href='/searchStudent'>Search Student By ID </a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(f"<h3>Course have been added with ID {next_id}</h3>".encode('utf-8'))
                self.wfile.write(b"<div><a href='/addCourse'>Add A New Course</a></div>")
                self.wfile.write(b"</center></body></html>")

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

        return

    def do_GET(self):
        try:

            if self.path == '/':
                data = []
                records = self.database.getAllStudents()
                for record in records:
                    data = record.fetchall()

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Teacher's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Teacher's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addStudent'>Add Student</a>|\
                                  <a href='/addCourse'>Add Course</a>|\
                                  <a href='/searchStudent'>Search Student By ID </a></div>")
                self.wfile.write(b"<hr><h2>All Students With Grade</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th>Student Name </th>\
                                        <th> Student ID </th>\
                                        <th> Course Name </th>\
                                        <th> Grade </th></tr>")
                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(row[1].encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(row[5].encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return
            if self.path == '/addStudent':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Teacher's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Teacher's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addStudent'>Add Student</a>|\
                                  <a href='/addCourse'>Add Course</a>|\
                                  <a href='/searchStudent'>Search Student By ID </a></div>")
                self.wfile.write(b"<hr><h2>Add New Student</h2>")

                self.wfile.write(b"<form action='/addStudent' method='post'>")
                self.wfile.write(b'<label for="sname">Student Name:</label>\
                      <input type="text" id="sname" name="sname"><br><br>\
                      <label for="courseid">course id:</label>\
                      <input type="number" id="courseid" name="courseid"><br><br>\
                      <label for="sgrade">Grade:</label>\
                      <input type="text" id="sgrade" name="sgrade"><br><br>\
                      <input type="submit" value="Submit">\
                      </form>')

                self.wfile.write(b"</center></body></html>")
                return
            if self.path == '/addCourse':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Teacher's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Teacher's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addStudent'>Add Student</a>|\
                                  <a href='/addCourse'>Add Course</a>|\
                                  <a href='/searchStudent'>Search Student By ID </a></div>")
                self.wfile.write(b"<hr><h2>Add New Course</h2>")

                self.wfile.write(b"<form action='/addCourse' method='post'>")
                self.wfile.write(b'<label for="cname">Course Name:</label>\
                      <input type="text" id="cname" name="cname"><br><br>\
                      <input type="submit" value="Submit">\
                      </form>')

                self.wfile.write(b"</center></body></html>")
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)
        except Exception as e:
            print(e)

            if self.path == '/searchStudent':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Teacher's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Teacher's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addStudent'>Add Student</a>|\
                                  <a href='/addCourse'>Add Course</a>|\
                                  <a href='/searchStudent'>Search Student By ID </a></div>")
                self.wfile.write(b"<hr><h2>Search Student</h2>")

                self.wfile.write(b"</center></body></html>")
                return

            if self.path == '/modifyStudent':
                return


def run(server_class=HTTPServer, handler_class=PortalServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()


run()