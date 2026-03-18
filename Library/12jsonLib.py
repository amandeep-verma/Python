import json

jsonData = '''
{
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "Data Analysis", "Machine Learning"],
    "employed": null
}
'''

# Load JSON data to a Python dictionary
data = json.loads(jsonData)

data["location"] = "USA"

print(data)

# Loading python dictionary to JSON string
convertedJsonData = json.dumps(data, indent=4)
print(convertedJsonData)

# Loading json data from a file
with open('data.json', 'r') as file:
    fileData = json.load(file)
    print(fileData)