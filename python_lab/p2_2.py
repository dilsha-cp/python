import sqlite3
from sqlite3 import Error
def connect_to_sqlite(db_file):
    #to create a database connection
    conn=None
    try:
        conn=sqlite3.connect(db_file)
        print(f"connect to sqlite,sqlite version{sqlite3.version}")
        #to create a new sqlite cursor
        cursor=conn.cursor()
        #to create a table
        cursor.execute('''CREATE  TABLE IF NOT EXISTS user(
                       id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL);''')
        #to insert  a new row
        cursor.execute("INSERT INTO user(name)Values('dilsha')")
        #commit the transaction
        conn.commit()
        #to get row from table
        cursor.execute("SELECT * FROM user;")
        rows=cursor.fetchall()
        print("Data from the user table:")
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()
            print("sqlite connection is closed")
if __name__=="__main__":
    db_path="test_database.db"
    connect_to_sqlite(db_path)        