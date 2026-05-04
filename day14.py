import json

# Dictionary → JSON
data = {"name": "Sara", "marks": 90}
json_data = json.dumps(data)
print(json_data)

# JSON → Dictionary
json_string = '{"name": "Sara", "marks": 90}'
data = json.loads(json_string)
print(data)

# Write JSON to file
with open("data.json", "w") as file:
    json.dump(data, file)

# Read JSON from file
with open("data.json", "r") as file:
    data = json.load(file)
print(data)

import csv

# Write CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "marks"])
    writer.writerow(["John", 80])
    writer.writerow(["Sara", 90])

# Read CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

   
