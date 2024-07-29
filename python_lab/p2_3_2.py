#crud operation using mysql
# import
import mysql.connector
from mysql.connector import Error
#setting path
db_config={
    'host':'localhost',
    'user':'root',
    'password':'',
    'database':'sample'
}
#connect to database
def create_connection(config):
    conn=None
    try:
        conn=mysql.connector.connect(**config)
        if conn.is_connected():
            print("connection established")
    except Error as e:
        print(e)
    return conn
#create table
def create_table(conn):
    try:
        cmd='''CREATE TABLE IF NOT EXISTS users(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
        );
        '''
        cursor=conn.cursor()
        cursor.execute(cmd)
        conn.commit()
    except Error as e:
        print(e)
#insert value to table
def insert_student(conn,student):
    try:
        cmd='''INSERT INTO users (name,email) VALUES (%s,%s)'''
        cursor=conn.cursor()
        cursor.execute(cmd,student)
        conn.commit()
        print('student inserted')
    except Error as e:
        print(e)
# read values
def read_student(conn):
    try:
        cmd="SELECT * FROM users"
        cursor=conn.cursor()
        cursor.execute(cmd)
        rows=cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)
#update value
def update_student(conn,student_id,new_name):
    try:
        cmd=''''UPDATE users SET name=%s WHERE id=%s'''
        cursor=conn.cursor()
        cursor.execute(cmd,(new_name,student_id))
        conn.commit()
        print("student updated")
    except Error as e:
        print(e)
# delete values
def delete_student(conn,student_id):
    try:
        cmd="DELETE FROM user WHERE id=%s"
        cursor=conn.cursor()
        cursor.execute(cmd,(student_id))
        conn.commit()
        print("student deleted")
    except Error as e:
        print(e)
def main():
    # db connection created
    conn=create_connection(db_config)
    if conn is not None:
        #create table
        create_table(conn)
        #insert value
        insert_student(conn,('anshad muhammed','mca2336@gmail.com'))
        insert_student(conn,('dilsha basheer','mca2318@gmail.com'))
        #read and display
        print('Student befre update:\n')
        read_student(conn)
        #update a student
        update_student(conn,1,'anshad basheer')
        #display after update
        print('student after update:\n')
        read_student(conn)
        delete_student(conn,2)
        print('student after deleteion:\n')
        read_student(conn)
        conn.close()
    else:
        print('Error cant create the database connection')
if __name__=='__main__':
    main()


