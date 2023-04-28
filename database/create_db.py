import sys
import os

from database.database_functions.read_json import read_json
from database.database_functions.get_file_path import get_file_path
from database.database_functions.create_table import create_table
from database.database_functions.create_connection import create_connection
from database.database_functions.insert_us_cities import insert_us_cities
from database.database_functions.insert_world_cities import insert_world_cities
from database.database_functions.insert_growth import insert_growth
from database.database_functions.insert_metro_systems import insert_metro_systems
from database.database_functions.create_us_city_class_table import create_us_city_class_table, insert_us_city_class_data
from database.database_functions.create_world_city_class_table import create_world_city_class_table, insert_world_city_class_data

# add the parent directory to the path so we can import the file_functions module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# main function to create the database and tables
def main():
    database = get_file_path("city_data.db")

    # create the tables
    print('Creating the us_cities table...')
    us_city_table = """CREATE TABLE IF NOT EXISTS us_cities (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            country TEXT NOT NULL,
                            state TEXT NOT NULL,
                            countryCode TEXT NOT NULL,
                            latitude REAL NOT NULL,
                            longitude REAL NOT NULL,
                            population INTEGER NOT NULL,
                            area REAL NOT NULL
                        );"""

    print('Creating the world_cities table...')
    world_city_table = """CREATE TABLE IF NOT EXISTS world_cities (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            name2 TEXT,
                            country TEXT NOT NULL,
                            countryCode TEXT NOT NULL,
                            latitude REAL NOT NULL,
                            longitude REAL NOT NULL,
                            population INTEGER NOT NULL,
                            area REAL NOT NULL
                          );"""
    
    print('Creating the metro_systems table...')
    metro_table = """CREATE TABLE IF NOT EXISTS metro_systems (
                        id INTEGER PRIMARY KEY,
                        city TEXT NOT NULL,
                        country_region TEXT NOT NULL,
                        name TEXT NOT NULL,
                        service_opened INTEGER NOT NULL,
                        last_expanded INTEGER NOT NULL,
                        stations INTEGER NOT NULL,
                        system_length REAL NOT NULL,
                        annual_ridership REAL,
                        rail_type TEXT NOT NULL
                     );"""
    
    print('Creating the growth table...')
    growth_table = """CREATE TABLE IF NOT EXISTS growth (
                        id INTEGER PRIMARY KEY,
                        pop2023 INTEGER NOT NULL,
                        pop2022 INTEGER NOT NULL,
                        city TEXT NOT NULL,
                        country TEXT NOT NULL,
                        growthRate REAL NOT NULL,
                        type TEXT NOT NULL,
                        rank INTEGER NOT NULL,
                        state TEXT
                      );"""

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, us_city_table)
        create_table(conn, world_city_table)
        create_table(conn, metro_table)
        create_table(conn, growth_table)

        # Read the JSON files and import the data into the tables
        us_cities_data = read_json(get_file_path("usCityList.json"))
        insert_us_cities(conn, us_cities_data)
        
        world_cities_data = read_json(get_file_path("worldCityList.json"))
        insert_world_cities(conn, world_cities_data)

        metro_systems_data = read_json(get_file_path("metroList.json"))
        insert_metro_systems(conn, metro_systems_data)

        growth_data = read_json(get_file_path("growth.json"))
        insert_growth(conn, growth_data)

        # Create the us_city_class table and insert the data
        create_us_city_class_table(conn)
        insert_us_city_class_data(conn)
        create_world_city_class_table(conn)
        insert_world_city_class_data(conn)
        print()
        
        conn.commit()
    else:
        print("Error! Cannot create the database connection.")

    

if __name__ == "__main__":
    main()