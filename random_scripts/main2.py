import json
import os

def get_file_path(file_name):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(script_dir, file_name)

def read_json_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

def write_json_file(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def main():
    metro_list = read_json_file(get_file_path('metroList.json'))

    metro_list_with_id = []
    metro_list_without_id = []

    for metro in metro_list:
        if "id" in metro:
            metro_list_with_id.append(metro)
        else:
            metro_list_without_id.append(metro)

    write_json_file(get_file_path('metroListWithID.json'), metro_list_with_id)
    write_json_file(get_file_path('metroListWithoutID.json'), metro_list_without_id)

if __name__ == '__main__':
    main()
