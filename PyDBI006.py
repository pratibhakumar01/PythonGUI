#from getpass import getpass
#from mysql.connector import connect, Error

import mysql.connector

def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='root',
                                         password='Mason@012023')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def create_table():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE Hospital (Hospital_Id INTEGER NOT NULL PRIMARY KEY, Hospital_Name TEXT NOT NULL, Bed_Count INTEGER NOT NULL);")
        print("Table created successfully")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

def insert_into_table():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_insert_query = ("""INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count) VALUES (%s,%s,%s)""")
        #row_inserted = cursor.fetchall()
        tuple_3 = (3, 'Mercy Health', 500)
        tuple_4 = (4, 'Tri Health', 10000)
        tuple_6 = (6, 'Beacon Health', 150)
        cursor.execute(sql_insert_query, tuple_3)
        cursor.execute(sql_insert_query, tuple_4)
        cursor.execute(sql_insert_query, tuple_6)
        connection.commit()
        print("Inserted 3 rows into the Hospital table")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)


#create_table()
insert_into_table()
