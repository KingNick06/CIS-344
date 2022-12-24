import mysql.connector
from mysql.connector import Error


class Database():
    def __init__(self,
                 host="localhost",
                 port="8088",
                 database="teachers_portal",
                 user='root',
                 password='password'):

        self.host       = host
        self.port       = port
        self.database   = database
        self.user       = user
        self.password   = password
        self.connection = None
        self.cursor     = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host         = self.host,
                port         = self.port,
                database     = self.database,
                user         = self.user,
                password     = self.password)
            
            if self.connection.is_connected():
                return
        except Error as e:
            print("Error while connecting to MySQL", e)
    

    def getAllStudents(self):
        if self.connection.is_connected():
            self.cursor= self.connection.cursor();
            self.cursor.callproc("studentsWithGrade")
            records = self.cursor.stored_results()
            return records

    def addStudent(self, name, courseID , grade=0):
        ''' Complete the method to insert the student to
            students table'''
        self.cursor = self.connection.cursor()
        add_student = "insert into students(studentName, enrolledInCourseID, grade) values (%s, %s, %s)"
        self.cursor.execute(add_student, (name, courseID, grade))
        self.connection.commit()
        self.connection.close()
    def addCourse(self, name):
        self.cursor = self.connection.cursor()
        add_course = "insert into courses(courseName) values (%s)"
        self.cursor.execute(add_course, (name,))
        self.connection.commit()
        self.connection.close()
    def modifyGrade(self, studentID, grade):
        ''' Complete the method to update the grade of the student'''
        pass
    def showCourses(self, studentid):
        if self.connection.is_connected():
            self.cursor= self.connection.cursor();
            self.cursor.callproc("showStudent", args= (studentid,))
            records = self.cursor.stored_results()
            return records
