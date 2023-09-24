import json

json_file_name = "random.json"
with open(json_file_name) as json_file:
    data = json.load(json_file)
    print(data)

    first_name = data["firstname"]
    last_name = data["lastname"]
    print(f"first name is: {first_name}")
    print(f"last name is: {last_name}")




