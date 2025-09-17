import json

with open('r1.json') as file:
    json_data = json.load(file)

print(json_data['router']['interfaces'][0])