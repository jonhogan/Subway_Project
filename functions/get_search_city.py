# function the ask the user to enter a city they want to search for and returns it


def get_search_city(us_list, world_list):
  #loop until the input is correct
  while True:
    city_name = input("Which city would you like to search for?")
    if city_name.isalpha():
      break
    else:
      print("Invalid city name. City name must be all alpha characters")

  # bool to control the search of the second city list
  city_found = False

  for city in us_list:
    if city_name == city.name:
      city_found = True
      return city

  if not city_found:
    for city in world_list:
      if city_name == city.name or city == city.name2:
        city_found = True
        return city

  if not city_found:
    print("We do not have the information for that city.")
