#crud operation using sqlite
import sqlite3
db_path='C:\MCA\SEM3\python\python_lab\sample.db'
# function to connect to the database
def create_connection(db_file):
    conn=None
    try:
        conn=sqlite3.connect(db_file)
        print("Connection established")
    except sqlite3.Error as e:
        print(e)
    return conn
def create_table(conn):
    try:
        sql_create_table='''CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
        );
        '''
        conn.execute(sql_create_table)
        print("Table is created")
    except sqlite3.Error as e:
        print(e)
def insert_table(conn,student):
    try:
        sql_insert='''
        INSERT INTO users(name,email) VALUES(?,?)
        '''
        conn.execute(sql_insert,student)
        conn.commit()
        print("student inserted")
    except sqlite3.Error as e:
        print(e)
def read_student(conn):
    try:
        sql_select="SELECT * FROM users"
        cursor=conn.execute(sql_select)
        rows=cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)
def update_student(conn,student_id,new_name):
    try:
        sql_update="UPDATE users SET name=? WHERE id=?"
        conn.execute(sql_update,(new_name,student_id))
        conn.commit()
        print("student updated")
    except sqlite3.Error as e:
        print(e)
def delete_student(conn,student_id):
    try:
        sql_delete="DELETE FROM users WHERE id=?"
        conn.execute(sql_delete,(student_id))
        conn.commit()
        print("student deleted")
    except sqlite3.Error as e:
        print(e)
def main():
    #create a database connection
    conn=create_connection(db_path)
    # create table if needed
    if conn is not None:
        create_table(conn)
        #insert student
        insert_table(conn,('mariyappi','mariya@gmail.com'))
        insert_table(conn,('dilsha','dilsha@gmail.com'))
        #read and display
        print("student details before update")
        read_student(conn)
        #update a student 
        update_student(conn,1,'dilsha')
        #read and display 
        print("student after update")
        read_student(conn)
        #delete a student
        delete_student(conn,1)
        print("students after deletion:")
        read_student(conn)
        conn.close()
    else:
        print("Error! cant create the database connection")
if __name__=='__main__':
    main()
