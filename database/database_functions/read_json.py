import json

# function to read and return the contents of a json file
def read_json(file_name):
  with open(file_name, 'r', encoding='utf-8') as json_file:
    return json.load(json_file)