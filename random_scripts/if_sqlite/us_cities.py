import sqlite3
import json


# Function to create usCities table in the database
def create_us_cities_table(conn):
  cursor = conn.cursor()
  # Execute SQL query to create table if it doesn't exist
  cursor.execute('''
        CREATE TABLE IF NOT EXISTS usCities (
            id INTEGER PRIMARY KEY,
            name TEXT,
            country TEXT,
            state TEXT,
            countryCode TEXT,
            latitude REAL,
            longitude REAL,
            population INTEGER,
            area REAL
        )
    ''')
  conn.commit()


# Function to insert data from JSON file into the usCities table
def insert_us_cities(conn, json_data):
  cursor = conn.cursor()
  for city_data in json_data:
    # Execute SQL query to insert or replace data in the table
    cursor.execute(
      '''
            INSERT OR REPLACE INTO usCities (id, name, country, state, countryCode, latitude, longitude, population, area)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
      (city_data["id"], city_data["name"], city_data["country"],
       city_data["state"], city_data["countryCode"], city_data["latitude"],
       city_data["longitude"], city_data["population"], city_data["area"]))
  conn.commit()


def add_us_cities():
  # Connect to the database and create it in the "files" folder
  conn = sqlite3.connect('files/TAPP.db')

  # Create the usCities table
  create_us_cities_table(conn)

  # Read the JSON file and load the data
  with open('files/usCityList.json', 'r') as json_file:
    json_data = json.load(json_file)

  # Insert the JSON data into the usCities table
  insert_us_cities(conn, json_data)

  # Close the connection to the database
  conn.close()