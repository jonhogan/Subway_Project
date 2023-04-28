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
from functions.imports import decision_tree, create_connection, get_world_city_data
from functions.imports import add_world_city, add_us_city, get_min_max_values, get_growth_data

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

    # menu
    print('1: Look up a city')
    print('2: Add a city')
    print('3: Exit')

    # get user input and validate
    while True:
        choice = input('Enter your selection (1-3): ')

        if not choice.isdigit():
            print('Invalid selection')
        else:
            break

    choice = int(choice)
    temp_city = None

    if choice == 1:

        # get user input and validate
        while True:
            look_up_city = input(
                'Enter the name of the city you would like to look up: ')

            if look_up_city.isdigit():
                print('Invalid input. City names should be alpha only')

            elif look_up_city == "Washington":
                while True:
                    answer = input(
                        'Are you wanting to search for Washington, D.C.?: ').lower(
                        )

                    if answer in ('y', 'yes'):
                        look_up_city = "Washington, D.C."

                    elif answer in ('n', 'no'):
                        break
                    else:
                        print('Invalid option, please enter Y/N or Yes/No: ')

            else:
                break

        city_found = False
        results = ''

        for city in us_city_list:
            lower_city = city.name.lower()
            if look_up_city.lower() == lower_city:
                temp_city = city
                results = decision_tree(city, us_min_max)
                city_found = True
                print(f'\n{city}\n\n{results}')
                break

        if not city_found:
            for city in world_city_list:
                lower_city = city.name.lower()
                lower_city2 = city.name2.lower()
                if look_up_city.lower() == lower_city or look_up_city.lower(
                ) == lower_city2:
                    temp_city = city
                    results = decision_tree(city, world_min_max)
                    city_found = True
                    print(f'\n{city}\n\n{results}')
                    break

        if not city_found:
            print(
                'The city was not found in the database, you should think about adding it.'
            )
        else:
            while True:
                # Get temp data to test the city with a different population
                response = input(
                'Would you like to test the city with a different population?: ')

                if response.lower() in ('y', 'yes'):
                    while True:
                        temp_pop = input('Enter the new population: ')

                        if not temp_pop.isdigit():
                            print('Invalid input, population should be numeric')
                        else:
                            temp_city.population = int(temp_pop)
                            break

                    results = decision_tree(temp_city, us_min_max)
                    print(f'\n{city}\n\n{results}')

                elif response.lower() in ('n', 'no'):
                    if temp_city is not None:
                        del temp_city
                    break

                else:
                    print('Invalid input, please enter Y/N or Yes/No: ')

    elif choice == 2:
        is_us = input('Is the city in the United States?: ')

        if is_us.lower() in ('y', 'yes'):
            new_city = add_us_city(conn)
            us_city_list.append(new_city)

        elif is_us.lower() in ('n', 'no'):
            new_city = add_world_city(conn)
            world_city_list.append(new_city)

        else:
            print('\nInvalid input\n\n')

    elif choice == 3:
        print('Goom-bye')
        break

    else:
        print('\nInvalid input\n\n')
