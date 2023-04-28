import sqlite3

# functions to insert data into the us_cities_data table
def insert_us_cities(conn, us_cities_data):
    query = """
        INSERT INTO us_cities (id, name, country, state, countryCode, latitude, longitude, population, area)
        VALUES (:id, :name, :country, :state, :countryCode, :latitude, :longitude, :population, :area)
    """

    # convert the list of dictionaries to a list of tuples
    us_cities_tuples = []
    for city in us_cities_data:
        city_tuple = (city["id"], city["name"], city["country"], city["state"], city["countryCode"], city["latitude"], city["longitude"], city["population"], city["area"])
        us_cities_tuples.append(city_tuple)

    cursor = conn.cursor()
    
    # insert data to city_data, and check for any duplicate ids
    for city_tuple in us_cities_tuples:
        try:
            cursor.execute(query, city_tuple)
        except sqlite3.IntegrityError:
            print(f"Duplicate id found: US Cities: {city_tuple[0]}, , {city_tuple[1]}")
            continue
    conn.commit()