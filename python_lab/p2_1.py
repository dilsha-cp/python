import mysql.connector
from mysql.connector import errorcode
def connect_to_mysql():
    connection=None
    cursor=None
    try:
        connection=mysql.connector.connect(
            host='localhost',
            database='sample',
            user='root',
            password=''
        )
        if connection.is_connected():
            print("connected to Mysql Server")
            cursor=connection.cursor()
            # to fetch data from table
            cursor.execute("SELECT * FROM student;")
            rows=cursor.fetchall()
            print("Data from the table;")
            for row in rows:
                print(row)
            
    except Error as e:
        print("Error while connecting to mysql",e)
    finally:
        #To ensure the cursor and connection are closedd even if an error occurs
        if cursor is not None:
            cursor.close()
            print("my sql cursor is closed")
        if connection is not None and connection.is_connected():
            connection.close()
            print("my sql connection is closed")
if __name__=="__main__":
    connect_to_mysql()