"""
This module will create the database and tables for the city_data.db file.
It is only run is the city_data.db file does not exist.

    Parameters:
        conn: Connection object to the database
        create_table_sql: SQL statement to create the table

    Returns:
        None
"""

import sqlite3

def create_table(conn, create_table_sql):
    """
    Create a table from the create_table_sql statement
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as error:
        print(error)