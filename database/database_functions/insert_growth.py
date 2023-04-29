"""
This module contains the function to insert data into the growth table of
the database

    Parameters:
        conn (sqlite3.Connection): A connection to the database
        
"""

import sqlite3

def insert_growth(conn, growth_data):
    """
    Insert data into the growth table of the database
    """

    query = """INSERT INTO growth (
                   id, pop2023, pop2022, city, country, growthRate, type, rank, state
               ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    # convert the list of dictionaries to a list of tuples
    growth_tuples = []
    for city in growth_data:
        city_tuple = (city['id'], city['pop2023'], city['pop2022'], city['city'], city['country'], city['growthRate'],
                      city['type'], city['rank'], city['state'])
        growth_tuples.append(city_tuple)

    cursor = conn.cursor()

    # insert the data into the database and check for duplicates
    for city_tuple in growth_tuples:
        try:
            cursor.execute(query, city_tuple)
        except sqlite3.IntegrityError:
            print(f'Duplicate id found: Growth: {city_tuple[0]}, {city_tuple[3]}')
            continue
    conn.commit()