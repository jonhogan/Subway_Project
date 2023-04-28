"""
This module contains the add_world_city function, which prompts the user for information about a
new WorldCity and adds it to the database.
"""

import sqlite3
from classes.WorldCity import WorldCity
from functions.get_next_id import get_next_id

def add_world_city(conn):
    """
     Prompts the user for information about a new WorldCity and adds it to the database.

        Parameters:
            conn (Connection): Database connection object

        Returns:
            new_city (WorldCity): An instance of the WorldCity class
    """

    # get city information from the user
    name = input("Enter the name of the city: ")

    while True:
        try:
            pop = int(input("Enter the population of the city: "))
            break
        except ValueError:
            print("Invalid input. Population must be an integer value.\n")

    while True:
        try:
            area = float(input("Enter the area of the city in kilometers squared: "))
            break
        except ValueError:
            print("Invalid input. Area must be a numeric value (e.g. 123 or 123.4).\n")

    density = area / pop

    while True:
        try:
            growth = float(input("Enter the growth rate of the city (ex: 1% is .01): "))
            break
        except ValueError:
            print("Invalid input. Area must be a numeric value (e.g. 123 or 123.4).\n")

    while True:
        country = input("Enter the full name country of the city: ")
        if not country.isalpha():
            print("Invalid input. Country must be alpha characters.\n")
        else:
            break
    id_num = get_next_id(conn, name)

    # create a tuple of WorldCity to insert into the database
    city_tuple =  (id_num, name, name, country, pop, area, density, growth, "unknown")

    query = """
        INSERT INTO world_city_class (id, name, name2, country, population, area, population_density, growth_rate, rail_type)
        VALUES (:id, :name, :name2, :country, :population, :area, :population_density, :growth_rate, :rail_type)
    """


    # execute the query to add the new city to the us_city_class table
    while True:
        try:
            conn.execute(query, city_tuple)
            conn.commit()
            break
        except sqlite3.Error as error:
            print(f'Error adding city to the database: {error}\n')
            print('Retrying...')

    new_city = WorldCity(*city_tuple)

    return new_city
