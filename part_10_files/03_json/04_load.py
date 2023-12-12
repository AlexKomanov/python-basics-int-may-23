import json

with open("data_to_load.json", "r") as loaded_file:
    data_from_json = json.load(loaded_file)

print(data_from_json["total"])

for item in data_from_json["data"]:
    print(item["email"], end=" | ")
