#!/usr/bin/python3
"""
Main driver file for the Subway project. This file will be used to run the program.
"""

#pylint: disable=C0103

from classes.CityGrowth import CityGrowth
from classes.MetroCity import MetroCity
from classes.USCity import USCity
from classes.WorldCity import WorldCity
from database.create_db import main as create_db_main
from functions.imports import sys, os, get_us_city_data, get_file_path, get_metro_data
from functions.imports import create_connection, get_world_city_data, get_add_city
from functions.imports import get_min_max_values, get_growth_data, get_lookup_city
from functions.imports import get_user_choice

sys.path.append(os.path.join(os.path.dirname(__file__), 'classes'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'functions'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'database'))

# define the path to city_data
database = get_file_path("city_data.db")

# check if city_data exists, if not, create it
if not os.path.exists(database):
    print('Database was not found.\n')
    create_connection(database)
    # call the main function from create_db.py to create and populate city_data.db
    create_db_main()

# create a connection to city_data
conn = create_connection(database)

# get the data from city_data to create the class objects
us_city_data = get_us_city_data(conn)
world_city_data = get_world_city_data(conn)
growth_data = get_growth_data(conn)
metro_data = get_metro_data(conn)

# add class objects to corresponding lists
us_city_list = [USCity(*data) for data in us_city_data]
world_city_list = [WorldCity(*data) for data in world_city_data]
growth_list = [CityGrowth(*data) for data in growth_data]
metro_list = [MetroCity(*data) for data in metro_data]

# get min/max values for normalization
us_min_max = get_min_max_values(us_city_list)
world_min_max = get_min_max_values(world_city_list)

while True:

    choice = get_user_choice()

    if choice == 1:
        get_lookup_city(us_city_list, world_city_list, us_min_max, world_min_max)

    elif choice == 2:
        get_add_city(conn, us_city_list, world_city_list)

    elif choice == 3:
        print('Goom-bye')
        break

    else:
        print('\nInvalid input\n\n')
