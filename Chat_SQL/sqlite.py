
import sqlite3
# first need to run this file 
# this file will create new table and insert some records in that table and then we  will use this file in app.py
## connect to sqlite database
connection = sqlite3.connect("india.db")#ahiye j file name chhe e file name app.py ma pan hovu joie to j aa data avse 

## create a cursor object
cursor = connection.cursor()

## drop table if it already exists
cursor.execute("DROP TABLE IF EXISTS students")

## create a larger students table
table_info = """
CREATE TABLE students(
student_id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT,
last_name TEXT,
gender TEXT,
age INTEGER,
email TEXT,
phone TEXT,
city TEXT,
course TEXT,
department TEXT,
semester INTEGER,
cgpa REAL,
attendance REAL
)
"""

cursor.execute(table_info)

## insert records
cursor.execute("""
INSERT INTO students 
(first_name,last_name,gender,age,email,phone,city,course,department,semester,cgpa,attendance)
VALUES
('Rahul','Sharma','Male',21,'rahul@gmail.com','9876543210','Delhi','Computer Science','Engineering',5,8.5,92)
""")

# 8 more example student records inspired by notable contributors to India
cursor.execute("""
INSERT INTO students 
(first_name,last_name,gender,age,email,phone,city,course,department,semester,cgpa,attendance)
VALUES
('Bhagat','Singh','Male',22,'bhagat@gmail.com','9876543215','Punjab','Political Science','Arts',4,9.0,95)
""")

cursor.execute("""
INSERT INTO students 
(first_name,last_name,gender,age,email,phone,city,course,department,semester,cgpa,attendance)
VALUES
('Sardar','Patel','Male',23,'patel@gmail.com','9876543216','Gujarat','Civil Engineering','Engineering',5,8.8,92)
""")

cursor.execute("""
INSERT INTO students 
(first_name,last_name,gender,age,email,phone,city,course,department,semester,cgpa,attendance)
VALUES
('Rani','Lakshmibai','Female',21,'rani@gmail.com','9876543217','Jhansi','History','Arts',3,9.2,97)
""")

cursor.execute("""
INSERT INTO students 
(first_name,last_name,gender,age,email,phone,city,course,department,semester,cgpa,attendance)
VALUES
('Subhas','Chandra Bose','Male',24,'bose@gmail.com','9876543218','Kolkata','International Relations','Arts',6,8.7,93)
""")

cursor.execute("""
INSERT INTO students 
(first_name,last_name,gender,age,email,phone,city,course,department,semester,cgpa,attendance)
VALUES
('Dr.','APJ Abdul Kalam','Male',25,'kalam@gmail.com','9876543219','Rameswaram','Aerospace Engineering','Engineering',6,9.5,98)
""")



cursor.execute("""
INSERT INTO students 
(first_name,last_name,gender,age,email,phone,city,course,department,semester,cgpa,attendance)
VALUES
('Raja','Ram Mohan Roy','Male',22,'rammohan@gmail.com','9876543221','Bengal','Philosophy','Arts',4,9.1,96)
""")

cursor.execute("""
INSERT INTO students 
(first_name,last_name,gender,age,email,phone,city,course,department,semester,cgpa,attendance)
VALUES
('Dr.','B.R. Ambedkar','Male',24,'ambedkar@gmail.com','9876543222','Maharashtra','Law','Arts',6,9.3,97)
""")
## display records
print("The inserted records are:\n")

data = cursor.execute("SELECT * FROM students")

for row in data:
    print(row)

## commit changes
connection.commit()

## close connection
connection.close()




