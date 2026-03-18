# ============== SET BASICS ==============
# Sets hold unique values, unordered, and mutable
# Elements must be immutable (hashable): int, str, tuple, frozenset
# Cannot contain: list, dict, set

# Empty set - MUST use set(), not {}
mySet = set()              # Empty set
empty_dict = {}            # This creates empty DICT, not set!

# Creating sets
mySet = {1, 2, 3}          # {1, 2, 3}
mySet = set([1, 2, 2, 3])  # {1, 2, 3} (duplicates removed)

# ============== ADDING ELEMENTS ==============
mySet = {1, 2, 3}

# Add single element - O(1)
mySet.add(4)               # {1, 2, 3, 4}
mySet.add(2)               # {1, 2, 3, 4} (duplicate ignored)

# Add multiple elements - O(k)
mySet.update([5, 6])       # {1, 2, 3, 4, 5, 6}
mySet.update({7, 8})       # Can also use another set

# ============== REMOVING ELEMENTS ==============
mySet = {1, 2, 3, 4, 5}

# remove() - raises KeyError if not found - O(1)
mySet.remove(3)            # {1, 2, 4, 5}
# mySet.remove(10)         # KeyError!

# discard() - does NOT raise error if not found - O(1)
mySet.discard(4)           # {1, 2, 5}
mySet.discard(10)          # No error, set unchanged

# pop() - removes and returns arbitrary element - O(1)
element = mySet.pop()      # Returns and removes some element
# mySet.pop()              # Raises KeyError if set is empty

# clear() - removes all elements - O(n)
mySet.clear()              # set()

# ============== MEMBERSHIP & SIZE ==============
mySet = {1, 2, 3, 4, 5}

# Check membership - O(1) average (this is why sets are useful!)
print(3 in mySet)          # True
print(10 not in mySet)     # True

# Size
print(len(mySet))          # 5

# ============== SET OPERATIONS ==============
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

# Union (all elements from both sets)
print(setA | setB)         # {1, 2, 3, 4, 5, 6}
print(setA.union(setB))    # {1, 2, 3, 4, 5, 6}

# Intersection (common elements)
print(setA & setB)         # {3, 4}
print(setA.intersection(setB))  # {3, 4}

# Difference (in A but not in B)
print(setA - setB)         # {1, 2}
print(setA.difference(setB))    # {1, 2}

# Symmetric Difference (in A or B but not both)
print(setA ^ setB)         # {1, 2, 5, 6}
print(setA.symmetric_difference(setB))  # {1, 2, 5, 6}

# ============== SET COMPARISONS ==============
setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5}
setC = {1, 2, 3}

# Subset (all elements of A are in B)
print(setA.issubset(setB))      # True
print(setA <= setB)             # True

# Proper subset (subset but not equal)
print(setA < setB)              # True
print(setA < setC)              # False (equal sets)

# Superset (all elements of B are in A)
print(setB.issuperset(setA))    # True
print(setB >= setA)             # True

# Disjoint (no common elements)
print(setA.isdisjoint({4, 5}))  # True
print(setA.isdisjoint({3, 4}))  # False

# ============== ITERATION ==============
mySet = {1, 2, 3, 4, 5}

# Sets are unordered - iteration order is unpredictable
for item in mySet:
    print(item)

# Convert to sorted list for ordered iteration
for item in sorted(mySet):
    print(item)            # 1, 2, 3, 4, 5

# ============== VALID/INVALID ELEMENTS ==============
# ✅ Valid (immutable/hashable types)
mySet = {1, "hello", 3.14, (1, 2), True}

# ❌ Invalid (mutable types)
# mySet.add([1, 2])       # TypeError: unhashable type: 'list'
# mySet.add({1, 2})       # TypeError: unhashable type: 'set'
# mySet.add({'a': 1})     # TypeError: unhashable type: 'dict'

# ============== CONVERSIONS ==============
# List to set (removes duplicates)
myList = [1, 2, 2, 3, 3, 4]
mySet = set(myList)       # {1, 2, 3, 4}

# Set to list
myList = list(mySet)      # [1, 2, 3, 4] (order unpredictable)
myList = sorted(mySet)    # [1, 2, 3, 4] (sorted)

# String to set (unique characters)
chars = set("hello")      # {'h', 'e', 'l', 'o'}

# ============== COMMON PATTERNS ==============
# Remove duplicates from list
nums = [1, 2, 2, 3, 3, 4]
unique = list(set(nums))  # [1, 2, 3, 4]

# Check for common elements
list1 = [1, 2, 3]
list2 = [3, 4, 5]
has_common = bool(set(list1) & set(list2))  # True

# Find unique elements across multiple lists
all_unique = set(list1) | set(list2)  # {1, 2, 3, 4, 5}

# Count unique elements
count = len(set(nums))

# ============== FROZENSET ==============
# Immutable version of set - can be used as dict key or set element
fs = frozenset([1, 2, 3])
# fs.add(4)              # AttributeError: no add method

# Use in set or as dict key
mySet = {frozenset([1, 2]), frozenset([3, 4])}
myDict = {frozenset([1, 2]): "value"}

# ============== SET COMPREHENSION ==============
# Create set using comprehension
squares = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}

# With condition
evens = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}