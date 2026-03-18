# ============== DICTIONARY BASICS ==============
# Dictionaries store key-value pairs
# Keys must be immutable (str, int, float, tuple) and unique
# Values can be any type
# Maintains insertion order (Python 3.7+)

# Creating dictionaries
myDict = {}                           # Empty dict
myDict = {"name": "John", "age": 30}
myDict = dict(name="John", age=30)    # Using dict()

# ============== ACCESSING ELEMENTS ==============
myDict = {"name": "John", "age": 30, "city": "NYC"}

# Access by key
print(myDict["name"])                 # "John"
# print(myDict["country"])            # KeyError!

# get() - safer access (returns None if key not found)
print(myDict.get("name"))             # "John"
print(myDict.get("country"))          # None
print(myDict.get("country", "USA"))   # "USA" (default value)

# ============== ADDING/MODIFYING ELEMENTS ==============
myDict = {"name": "John"}

# Add or update
myDict["age"] = 30                    # Add new key
myDict["name"] = "Jane"               # Update existing key

# Update multiple items
myDict.update({"city": "NYC", "age": 31})
myDict.update(country="USA")          # Alternative syntax

# setdefault() - add if key doesn't exist, return value
val = myDict.setdefault("state", "CA")  # Adds "state": "CA", returns "CA"
val = myDict.setdefault("city", "LA")   # Key exists, returns "NYC", no change

# ============== REMOVING ELEMENTS ==============
myDict = {"name": "John", "age": 30, "city": "NYC"}

# pop() - remove and return value
age = myDict.pop("age")               # Returns 30, removes "age"
# val = myDict.pop("country")         # KeyError!
val = myDict.pop("country", "N/A")    # Returns "N/A" if key not found

# popitem() - remove and return last inserted key-value pair
item = myDict.popitem()               # Returns ("city", "NYC")

# del - delete specific key
del myDict["name"]

# clear() - remove all items
myDict.clear()                        # {}

# ============== CHECKING KEYS ==============
myDict = {"name": "John", "age": 30}

# Check if key exists
print("name" in myDict)               # True
print("city" not in myDict)           # True

# ============== ITERATION ==============
myDict = {"name": "John", "age": 30, "city": "NYC"}

# Iterate over keys (default)
for key in myDict:
    print(key)

# Iterate over keys explicitly
for key in myDict.keys():
    print(key)

# Iterate over values
for value in myDict.values():
    print(value)

# Iterate over key-value pairs
for key, value in myDict.items():
    print(f"{key}: {value}")

# ============== DICTIONARY METHODS ==============
myDict = {"name": "John", "age": 30, "city": "NYC"}

# Get all keys
keys = myDict.keys()                  # dict_keys(['name', 'age', 'city'])
keys_list = list(myDict.keys())       # Convert to list

# Get all values
values = myDict.values()              # dict_values(['John', 30, 'NYC'])

# Get all items
items = myDict.items()                # dict_items([('name', 'John'), ...])

# Length
print(len(myDict))                    # 3

# Copy
shallow_copy = myDict.copy()
import copy
deep_copy = copy.deepcopy(myDict)

# ============== SORTING DICTIONARIES ==============
#Dictionaries themselves do not have a sort method because they are inherently unordered collections.
# However, you can create a sorted representation of a dictionary's keys or items using the built-in sorted() function.
myDict = {"banana": 3, "apple": 5, "cherry": 1}

# Sort by keys (returns new dict)
sorted_by_keys = dict(sorted(myDict.items()))
# {'apple': 5, 'banana': 3, 'cherry': 1}

# Sort by values
sorted_by_values = dict(sorted(myDict.items(), key=lambda x: x[1]))
# {'cherry': 1, 'banana': 3, 'apple': 5}

# Reverse sort
sorted_desc = dict(sorted(myDict.items(), reverse=True))

# Get sorted keys/values as lists
sorted_keys = sorted(myDict.keys())
sorted_values = sorted(myDict.values())

# ============== DICTIONARY COMPREHENSION ==============
# Create dict from iterable
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition
evens = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
myDict = {k: v for k, v in zip(keys, values)}
# {'a': 1, 'b': 2, 'c': 3}

# ============== MERGING DICTIONARIES ==============
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Using update (modifies dict1)
dict1.update(dict2)               # dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using unpacking (Python 3.5+)
merged = {**dict1, **dict2}       # Creates new dict

# Using | operator (Python 3.9+)
merged = dict1 | dict2            # Creates new dict

# Overlapping keys - later dict wins
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}       # {'a': 1, 'b': 3, 'c': 4}

# ============== NESTED DICTIONARIES ==============
students = {
    "student1": {"name": "John", "age": 20},
    "student2": {"name": "Jane", "age": 22}
}

# Access nested values
print(students["student1"]["name"])   # "John"

# Safely access nested values
name = students.get("student1", {}).get("name", "Unknown")

# ============== DEFAULTDICT ==============
from collections import defaultdict

# With list as default
dd = defaultdict(list)
dd["fruits"].append("apple")      # Auto-creates empty list
dd["fruits"].append("banana")
# defaultdict(<class 'list'>, {'fruits': ['apple', 'banana']})

# With int as default (useful for counting)
counter = defaultdict(int)
for char in "hello":
    counter[char] += 1            # Auto-initializes to 0
# defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 2, 'o': 1})

# With set as default
dd = defaultdict(set)
dd["nums"].add(1)
dd["nums"].add(2)



testDict = defaultdict(list)  # default value is an empty list

testDict["one"].append(1)  # Now this works fine
print(testDict)  # defaultdict(<class 'list'>, {'one': [1]
print(testDict["two"])  # Accessing non-existing key returns default empty list [], creates key "two" with []
print(testDict)  # defaultdict(<class 'list'>, {'one': [1]

# You can achieve similar behavior using get() method with default value
standardDict = {}
# standardDict["one"] = standardDict.get("one", []).append(1)  # COMMON MISTAKE - Since append() returns None, this sets standardDict["one"] to None
standardDict["one"] = standardDict.get("one", []) + [1]  # Correct way to append
standardDict["one"] = standardDict.get("one", []) + [2]  # appends 2 to existing list

# OR
if "one" not in standardDict:
    standardDict["one"] = []
standardDict["one"].append(3)

# OR
standardDict.setdefault("one", []).append(4)
print("corrected",standardDict)  # {'one': [1, 2, 3, 4]}


# Custom default function
dd = defaultdict(lambda: "N/A")
print(dd["missing"])              # "N/A"

# ============== COUNTER ==============
from collections import Counter

# Count occurrences
text = "hello world"
counts = Counter(text)
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Most common elements
print(counts.most_common(2))      # [('l', 3), ('o', 2)]

# Counter arithmetic
c1 = Counter(['a', 'b', 'c', 'a'])
c2 = Counter(['a', 'b', 'd'])
print(c1 + c2)                    # Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
print(c1 - c2)                    # Counter({'a': 1, 'c': 1})

# ============== COMMON PATTERNS ==============
# Frequency counter (manual)
text = "hello"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1

# Group by property
words = ["apple", "banana", "apricot", "blueberry"]
grouped = {}
for word in words:
    key = word[0]                 # Group by first letter
    grouped.setdefault(key, []).append(word)
# {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}

# Invert dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}

# Filter dictionary
original = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered = {k: v for k, v in original.items() if v > 2}
# {'c': 3, 'd': 4}

# ============== IMPORTANT NOTES ==============
# Keys must be immutable
# valid_dict = {(1, 2): "tuple key"}   # ✅ Tuple is immutable
# invalid_dict = {[1, 2]: "list key"}  # ❌ TypeError: list is not hashable

# Dictionaries are compared by content, not order
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}
print(dict1 == dict2)             # True

# Get with setdefault vs defaultdict
# setdefault: use for one-time default on regular dict
# defaultdict: use when you need default for all missing keys