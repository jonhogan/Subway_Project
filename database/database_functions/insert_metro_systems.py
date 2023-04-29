"""
This module contains the function to insert data into the metro_systems table of
the database

    Parameters:
        conn (sqlite3.Connection): A connection to the database
        metro_systems_data (list): A list of dictionaries containing the data to be inserted

    Returns:
        None
"""
import sqlite3

def insert_metro_systems(conn, metro_systems_data):
    """
    Functions to insert data into the metro_systems_data table
    """
    query = """INSERT INTO metro_systems (
                    id, city, country_region, name, service_opened, last_expanded, stations, system_length,
                    annual_ridership, rail_type
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    # convert the list of dictionaries to a list of tuples
    metro_systems_tuples = []
    for city in metro_systems_data:
        city_tuple = (city["id"], city["City"], city["Country Region"], city["Name"], city["Service Opened"],
                       city["Last Expanded"], city["Stations"], city["System Length (km)"], city["Annual Ridership (millions)"],
                       city["Rail Type"])
        metro_systems_tuples.append(city_tuple)

    cursor = conn.cursor()

    # insert data to the table and check for any duplicate ids
    for city_tuple in metro_systems_tuples:
        try:
            cursor.execute(query, city_tuple)
        except sqlite3.IntegrityError:
            print(f"Duplicate id found: Metro: {city_tuple[0]}, {city_tuple[1]}")
            continue
    conn.commit()