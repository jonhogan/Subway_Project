import json
from collections import OrderedDict
import os

def get_file_path(file_name):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(script_dir, file_name)

def read_json_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

def main():
    us_city_list = read_json_file(get_file_path('usCityList.json'))
    metro_list = read_json_file(get_file_path('metroList.json'))

    city_id_map = {city["name"]: city["id"] for city in us_city_list}

    updated_metro_list = []
    for metro in metro_list:
        if metro["City"] in city_id_map:
            updated_metro = OrderedDict()
            updated_metro["id"] = city_id_map[metro["City"]]
            for key, value in metro.items():
                updated_metro[key] = value
            updated_metro_list.append(updated_metro)
        else:
            updated_metro_list.append(metro)

    with open(get_file_path('updatedMetroList.json'), 'w', encoding='utf-8') as outfile:
        json.dump(updated_metro_list, outfile, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()