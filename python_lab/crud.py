#!C:\Users\cclab44\AppData\Local\Programs\Python\Python310\python.exe
import cgi
import mysql.connector
import html

print("Content-type: text/html\n\n")

# Connect to MySQL database
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'login'
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Retrieve form data
form = cgi.FieldStorage()
action = form.getvalue("action")
id = form.getvalue("id")
name = form.getvalue("name")
age = form.getvalue("age")
gender = form.getvalue("gender")
salary = form.getvalue("salary")

# HTML header
print("<html>")
print("<head>")
print("<title>CRUD Operations Result</title>")
print("</head>")
print("<body>")

if action == "create":
    if id and name and age and gender and salary:
        cursor.execute('''
            INSERT INTO employees (id,name, age, gender, salary)
            VALUES (%s,%s, %s, %s, %s)
        ''', (id,name, age, gender, salary))
        conn.commit()
        print(f"<p>Record created successfully for {html.escape(name)}.</p>")
    else:
        print("<p>Missing data for creating a record.</p>")

elif action == "read":
    cursor.execute('SELECT * FROM employees')
    records = cursor.fetchall()
    print("<h2>Employees List</h2>")
    print("<ul>")
    for row in records:
        print(f"<li>{html.escape(str(row))}</li>")
    print("</ul>")

elif action == "update":
    if id and name and age and gender and salary:
        cursor.execute('''
            UPDATE employees
            SET name = %s, age = %s, gender = %s, salary = %s
            WHERE id = %s
        ''', (name, age, gender, salary, id))
        conn.commit()
        print(f"<p>Record with ID {html.escape(id)} updated successfully.</p>")
    else:
        print("<p>Missing data for updating a record.</p>")

elif action == "delete":
    if id:
        cursor.execute('DELETE FROM employees WHERE id = %s', (id,))
        conn.commit()
        print(f"<p>Record with ID {html.escape(id)} deleted successfully.</p>")
    else:
        print("<p>Missing ID for deleting a record.</p>")

else:
    print("<p>Invalid action.</p>")

# Close the HTML tags
print("</body>")
print("</html>")

# Close the database connection
cursor.close()
conn.close()
