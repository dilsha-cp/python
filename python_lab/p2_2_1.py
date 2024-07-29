import sqlite3
#path to existing database
db_path='C:\MCA\SEM3\python\python_lab\sample.db'
#connect to the database
conn=sqlite3.connect(db_path)
#create a cursor object
cursor=conn.cursor()
#create table
cursor.execute('''CREATE TABLE IF NOT EXISTS student(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               email TEXT NOT NULL);''')
#insert data into table
students = [
    
    ("Alice", "alice@example.com"),
    ("Bob", "bob@example.com"),
    ("Charlie", "charlie@example.com")
]

# Insert multiple rows using executemany()
cursor.executemany("INSERT INTO student (name, email) VALUES (?, ?)", students)
# query data from table
cursor.execute("SELECT * FROM student")
stud=cursor.fetchall()
#print out the data
for students in stud:
    print(students)
#commit the transaction
conn.commit()
#to close the connection
conn.close()

