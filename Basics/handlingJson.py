# convert null in json to None in python
import json
json_data = '{"name": "John", "age": null, "city": "New York"}'
data = json.loads(json_data)
print(data)  # {'name': 'John', 'age': None, 'city':
print(data['age'] is None)  # True

# convert None in python to null in json
python_data = {"name": "Jane", "age": None, "city": "Los Angeles"}
json_data = json.dumps(python_data)
print(json_data)  # {"name": "Jane", "age": null, "city: "Los Angeles"}  


# Range
print("Range examples:", list(range(5)), list(range(2, 10)), list(range(1, 10, 2)))

simpleArray = [1, 2, 3, 4, 5, 6]
for i in range(0,len(simpleArray),2):
    print("Index:", i, "Value:", simpleArray[i])