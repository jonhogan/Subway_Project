"""
This module will create the us_city_class table for the city_data.db file.

    Functions:
        create_us_city_class_table: Creates the us_city_class table.
        insert_us_city_class_data: Inserts data into the us_city_class table.

    Parameters:
        conn: Connection object to the database

    Returns:
        None
"""

def create_us_city_class_table(conn):
    """
    Function to create the us_city_class table
    """

    create_table_query = """
        CREATE TABLE IF NOT EXISTS us_city_class (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            state TEXT NOT NULL,
            population INTEGER NOT NULL,
            area REAL NOT NULL,
            population_density REAL NOT NULL,
            growth_rate TEXT NOT NULL,
            rail_type TEXT NOT NULL
        );
    """

    cursor = conn.cursor()
    cursor.execute(create_table_query)
    conn.commit()
    print('Creating the us_city_class table...')

def insert_us_city_class_data(conn):
    """
    Function to insert data into the us_city_class table
    """
    """
    query us_cities, growth, and metro_systems tables and
    insert the data into the us_city_class table
    
    id, name, state, population and area from us_cities
    calculate population_density from us_cities
    growth_rate from growth
    rail_type from metro_systems
    """
    insert_data_query = """
        INSERT INTO us_city_class (
            id,
            name,
            state,
            population,
            area,
            population_density,
            growth_rate,
            rail_type
        )
        SELECT
            us_cities.id,
            us_cities.name,
            us_cities.state,
            us_cities.population,
            us_cities.area,
            ROUND(CAST(us_cities.population as REAL) / us_cities.area, 2) as population_density,
            COALESCE(growth.growthRate, 0.0) as growthRate,
            COALESCE(metro_systems.rail_type, 'Unknown') as rail_type
        FROM
            us_cities
        LEFT JOIN
            growth ON us_cities.name = growth.city AND us_cities.state = growth.state
        LEFT JOIN
            metro_systems ON us_cities.name = metro_systems.city;
    """

    cursor = conn.cursor()
    cursor.execute(insert_data_query)
    conn.commit()
    print('Inserting data into us_city_class table...')
