import sqlite3

# function to create a table in the database
def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as error:
        print(error)