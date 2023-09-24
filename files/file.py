import json

json_file_name = "random.json"
with open(json_file_name) as json_file:
    data = json.load(json_file)
    print(data)