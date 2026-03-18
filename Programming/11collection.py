# ============== COUNTER ==============
# Counter - dict subclass for counting hashable objects
from collections import Counter

# Create Counter from iterable
text = "hello world"
counter = Counter(text)
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# From list
nums = [1, 2, 2, 3, 3, 3, 4]
counter = Counter(nums)
# Counter({3: 3, 2: 2, 1: 1, 4: 1})

# From string with specific elements
counter = Counter(['apple', 'banana', 'apple', 'cherry', 'banana', 'apple'])
# Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# ============== COUNTER - ACCESSING COUNTS ==============
counter = Counter(['a', 'b', 'a', 'c', 'a', 'b'])

# Access count (returns 0 for missing keys, not KeyError)
print(counter['a'])         # 3
print(counter['z'])         # 0 (not KeyError!)

# Get most common elements
print(counter.most_common())      # [('a', 3), ('b', 2), ('c', 1)]
print(counter.most_common(2))     # [('a', 3), ('b', 2)]

# Get all elements (as iterator)
print(list(counter.elements()))   # ['a', 'a', 'a', 'b', 'b', 'c']

# Total count of all elements
print(sum(counter.values()))      # 6

# ============== COUNTER - OPERATIONS ==============
c1 = Counter(['a', 'b', 'c', 'a'])
c2 = Counter(['a', 'b', 'd'])

# Addition (combine counts)
print(c1 + c2)              # Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})

# Subtraction (subtract counts, keep only positive)
print(c1 - c2)              # Counter({'a': 1, 'c': 1})

# Intersection (min of corresponding counts)
print(c1 & c2)              # Counter({'a': 1, 'b': 1})

# Union (max of corresponding counts)
print(c1 | c2)              # Counter({'a': 2, 'b': 1, 'c': 1, 'd': 1})

# ============== COUNTER - UPDATING ==============
counter = Counter(['a', 'b', 'c'])

# Update (add counts)
counter.update(['a', 'b', 'd'])
# Counter({'a': 2, 'b': 2, 'c': 1, 'd': 1})

# Subtract (subtract counts, can go negative)
counter.subtract(['a', 'b'])
# Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1})

# ============== COUNTER - COMMON PATTERNS ==============
# Character frequency
text = "hello"
freq = Counter(text)        # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

# Word frequency
sentence = "the quick brown fox jumps over the lazy dog"
word_freq = Counter(sentence.split())
# Counter({'the': 2, 'quick': 1, 'brown': 1, ...})

# Find duplicates
nums = [1, 2, 2, 3, 3, 3, 4]
duplicates = [num for num, count in Counter(nums).items() if count > 1]
# [2, 3]

# Check if two strings are anagrams
s1, s2 = "listen", "silent"
is_anagram = Counter(s1) == Counter(s2)  # True

# ============== DEFAULTDICT ==============
# defaultdict - dict that provides default value for missing keys
from collections import defaultdict

# With list as default factory
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
# defaultdict(<class 'list'>, {'fruits': ['apple', 'banana']})

# With int as default factory (useful for counting)
counter = defaultdict(int)
for char in "hello":
    counter[char] += 1
# defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 2, 'o': 1})

# With set as default factory
dd = defaultdict(set)
dd['nums'].add(1)
dd['nums'].add(2)
# defaultdict(<class 'set'>, {'nums': {1, 2}})

# With custom default function
dd = defaultdict(lambda: 'N/A')
print(dd['missing'])        # 'N/A'

# ============== DEFAULTDICT - COMMON PATTERNS ==============
# Group items by property
words = ['apple', 'banana', 'apricot', 'blueberry', 'cherry']
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)
# defaultdict(<class 'list'>, {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']})

# Build adjacency list (graph)
edges = [(1, 2), (1, 3), (2, 4), (3, 4)]
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
# defaultdict(<class 'list'>, {1: [2, 3], 2: [4], 3: [4]})

# Count occurrences by category
data = [('apple', 'fruit'), ('carrot', 'veg'), ('banana', 'fruit')]
category_count = defaultdict(int)
for item, category in data:
    category_count[category] += 1
# defaultdict(<class 'int'>, {'fruit': 2, 'veg': 1})


# ============== ORDEREDDICT ==============
# OrderedDict - dict that remembers insertion order
# Note: Regular dicts maintain order in Python 3.7+, so OrderedDict is less necessary
from collections import OrderedDict

# Create OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
# OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Move key to end
od.move_to_end('a')         # OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# Move key to beginning
od.move_to_end('a', last=False)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Pop last item
item = od.popitem(last=True)     # ('c', 3)

# Pop first item
item = od.popitem(last=False)    # ('a', 1)

# ============== NAMEDTUPLE ==============
# namedtuple - tuple with named fields (immutable)
from collections import namedtuple

# Define namedtuple type
Point = namedtuple('Point', ['x', 'y'])

# Create instances
p1 = Point(10, 20)
p2 = Point(x=30, y=40)

# Access by name (more readable)
print(p1.x, p1.y)           # 10 20

# Access by index (still works like tuple)
print(p1[0], p1[1])         # 10 20

# Unpack
x, y = p1                   # x=10, y=20

# Convert to dict
print(p1._asdict())         # {'x': 10, 'y': 20}

# Replace (creates new instance, original unchanged)
p3 = p1._replace(x=50)      # Point(x=50, y=20)

# Common use cases
Person = namedtuple('Person', ['name', 'age', 'city'])
Student = namedtuple('Student', 'name grade school')  # Can use space-separated string

# Use in functions for clearer return values
def get_coordinates():
    Coordinate = namedtuple('Coordinate', ['lat', 'lon'])
    return Coordinate(37.7749, -122.4194)

coord = get_coordinates()
print(coord.lat, coord.lon)

# ============== CHAINMAP ==============
# ChainMap - combines multiple dicts into single view
from collections import ChainMap

# Create ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'c': 5, 'd': 6}

chain = ChainMap(dict1, dict2, dict3)

# Lookup - searches in order, returns first match
print(chain['a'])           # 1 (from dict1)
print(chain['b'])           # 2 (from dict1, not dict2)
print(chain['c'])           # 4 (from dict2, not dict3)
print(chain['d'])           # 6 (from dict3)

# All keys
print(list(chain.keys()))   # ['d', 'c', 'b', 'a']

# Updates affect first dict only
chain['a'] = 10
print(dict1)                # {'a': 10, 'b': 2}

# ============== COMPARISON: COUNTER vs DEFAULTDICT vs DICT ==============
# Counter - when you need to count occurrences
text = "hello"
Counter(text)               # Best for counting

# defaultdict - when you need default values for missing keys
dd = defaultdict(list)      # Best for grouping/accumulating

# Regular dict - when you don't need special behavior
d = {}                      # Most common, use by default

# ============== DEQUE vs LIST ==============
# Use deque when:
# - Need O(1) operations at both ends (append/pop from left)
# - Implementing queue or sliding window
# - Need maxlen for automatic trimming

# Use list when:
# - Need random access by index (lists are faster)
# - Only operating on right end (append/pop)
# - Need slicing operations