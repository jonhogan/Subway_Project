"""
This module will create the world_city_class table for the city_data.db file.

    Functions:
        create_world_city_class_table: Creates the world_city_class table.
        insert_world_city_class_data: Inserts data into the world_city_class table.

    Parameters:
        conn: Connection object to the database

    Returns:
        None
"""
def create_world_city_class_table(conn):
    """
    Function to create the world_city_class table
    """
    create_table_query = """
        CREATE TABLE IF NOT EXISTS world_city_class (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            name2 TEXT NOT NULL,
            country TEXT NOT NULL,
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
    print('Creating the world_city_class table...')

def insert_world_city_class_data(conn):
    """
    Function to insert data into the world_city_class table
    """
    """
    query world_cities, growth, and metro_systems tables and
    insert the data into the world_city_class table
    
    id, name, name2, country, population and area from world_cities
    calculate population_density from world_cities
    growth_rate from growth
    rail_type from metro_systems
    """
    insert_data_query = """
        INSERT INTO world_city_class (
            id,
            name,
            name2,
            country,
            population,
            area,
            population_density,
            growth_rate,
            rail_type
        )
        SELECT
            world_cities.id,
            world_cities.name,
            world_cities.name2,
            world_cities.country,
            world_cities.population,
            world_cities.area,
            ROUND(CAST(world_cities.population as REAL) / world_cities.area, 2) as population_density,
            COALESCE(growth.growthRate, 0.0) as growthRate,
            COALESCE(metro_systems.rail_type, 'Unknown') as rail_type
        FROM
            world_cities
        LEFT JOIN
            growth ON world_cities.id = growth.id
        LEFT JOIN
            metro_systems ON world_cities.id = metro_systems.id;
    """

    cursor = conn.cursor()
    cursor.execute(insert_data_query)
    conn.commit()
    print('Inserting data into world_city_class table...')
    