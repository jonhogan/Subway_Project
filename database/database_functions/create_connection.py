import sqlite3

# function to create a connection to the database
def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
    except sqlite3.Error as error:
        print(error)
    return conn
