# dictionary - key value pairs
mydict = {"name": "Amandeep", "age": 24, "city": "New Delhi"}
print(mydict)   

# making dictionary using zip function
list1 = ["name", "age", "city"]
list2 = ["Amandeep", 24, "New Delhi"]
mydict2 = dict(zip(list1, list2))
print(mydict2)

# accessing values using keys
print(mydict["name"])

# accessing values using get method
print(mydict.get("name"))
print(mydict.get("country", "India"))  # default value if key not found

# adding new key value pair
mydict["profession"] = "Developer"
print(mydict)

# accessing all keys
print("Keys:", mydict.keys())
# accessing all values
print("Values:", mydict.values())

for i,j in mydict.items():
    print(i, ":", j)    


testDict = {}

if "one" not in testDict:
    testDict["one"] = []
    


# testDict["one"].append(1)  # This will raise an AttributeError because the key "one" does not exist yet