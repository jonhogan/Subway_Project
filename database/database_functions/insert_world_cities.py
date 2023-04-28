import sqlite3

# function to insert data into the world_cities_data table
def insert_world_cities(conn, world_cities_data):
    query = """
        INSERT INTO world_cities (id, name, name2, country, countryCode, latitude, longitude, population, area)
        VALUES (:id, :name, :name2, :country, :countryCode, :latitude, :longitude, :population, :area)
    """

    # convert the list of dictionaries to a list of tuples
    world_cities_tuples = []
    for city in world_cities_data:
        city_tuple = (city["id"], city["name"], city["name2"], city["country"], city["countryCode"],
                      city["latitude"], city["longitude"], city["population"], city["area"])
        world_cities_tuples.append(city_tuple)

    cursor = conn.cursor()

    # insert data to the table and check for any duplicate ids
    for city_tuple in world_cities_tuples:
        try:
            cursor.execute(query, city_tuple)
        except sqlite3.IntegrityError:
            print(f"Duplicate id found: World Cities: {city_tuple[0]}, {city_tuple[1]}")
            continue
    conn.commit()