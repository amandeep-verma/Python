# ============== TUPLE BASICS ==============
# Tuples are immutable, ordered sequences
# Can store different data types
# Faster than lists, use less memory

# Creating tuples
a = (1, 2, 3, 4)
b = ('apple', 'banana', 'cherry')
c = (1, 'apple', 3.14, True)

# Single element tuple - MUST have trailing comma
single = (5,)              # Tuple with one element
not_tuple = (5)            # This is just an int: 5

# Empty tuple
empty = ()
empty = tuple()

# Tuple without parentheses (tuple packing)
t = 1, 2, 3                # (1, 2, 3)

# ============== ACCESSING ELEMENTS ==============
a = (10, 20, 30, 40, 50)

# Positive indexing
print(a[0])                # 10
print(a[2])                # 30

# Negative indexing
print(a[-1])               # 50
print(a[-2])               # 40

# ============== SLICING ==============
a = (10, 20, 30, 40, 50, 60, 70)

print(a[1:4])              # (20, 30, 40)
print(a[2:])               # (30, 40, 50, 60, 70)
print(a[:3])               # (10, 20, 30)
print(a[::2])              # (10, 30, 50, 70)
print(a[::-1])             # (70, 60, 50, 40, 30, 20, 10) (reversed)

# ============== IMMUTABILITY ==============
a = (1, 2, 3, 4)

# ❌ Cannot modify elements
# a[0] = 10                # TypeError: 'tuple' object does not support item assignment
# a.append(5)              # AttributeError: 'tuple' object has no attribute 'append'
# del a[0]                 # TypeError: 'tuple' object doesn't support item deletion

# ✅ Can reassign entire tuple
a = (5, 6, 7, 8)           # This is allowed (creating new tuple)

# ⚠️ Tuples with mutable elements
t = (1, 2, [3, 4])
# t[2] = [5, 6]           # TypeError
t[2].append(5)            # This works! → (1, 2, [3, 4, 5])
# The tuple itself is immutable, but mutable elements can change

# ============== TUPLE OPERATIONS ==============
t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation
combined = t1 + t2         # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = t1 * 3          # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# ============== TUPLE METHODS ==============
t = (1, 2, 3, 2, 4, 2, 5)

# count() - count occurrences - O(n)
print(t.count(2))          # 3

# index() - find first occurrence - O(n)
print(t.index(2))          # 1
print(t.index(2, 2))       # 3 (start searching from index 2)

# ============== MEMBERSHIP & SIZE ==============
t = (1, 2, 3, 4, 5)

# Check membership - O(n)
print(3 in t)              # True
print(10 not in t)         # True

# Length - O(1)
print(len(t))              # 5

# ============== UNPACKING ==============
# Basic unpacking
t = (1, 2, 3)
a, b, c = t                # a=1, b=2, c=3

# Swap variables
x, y = 5, 10
x, y = y, x                # x=10, y=5

# Extended unpacking (Python 3+)
t = (1, 2, 3, 4, 5)
first, *middle, last = t   # first=1, middle=[2,3,4], last=5
first, *rest = t           # first=1, rest=[2,3,4,5]
*rest, last = t            # rest=[1,2,3,4], last=5

# Ignore values with _
t = (1, 2, 3)
a, _, c = t                # a=1, c=3 (2 is ignored)

# ============== ITERATION ==============
t = (10, 20, 30, 40, 50)

# Direct iteration
for item in t:
    print(item)

# With index
for i, item in enumerate(t):
    print(f"Index {i}: {item}")

# ============== CONVERSIONS ==============
# List to tuple
lst = [1, 2, 3, 4]
t = tuple(lst)             # (1, 2, 3, 4)

# Tuple to list
t = (1, 2, 3, 4)
lst = list(t)              # [1, 2, 3, 4]

# String to tuple
s = "hello"
t = tuple(s)               # ('h', 'e', 'l', 'l', 'o')

# Range to tuple
t = tuple(range(5))        # (0, 1, 2, 3, 4)

# ============== COMPARING TUPLES ==============
# Tuples compared lexicographically (element by element)
print((1, 2, 3) < (1, 2, 4))    # True
print((1, 2, 3) == (1, 2, 3))   # True
print((1, 2) < (1, 2, 3))       # True (shorter is less)

# ============== BUILT-IN FUNCTIONS ==============
t = (3, 1, 4, 1, 5, 9, 2)

print(min(t))              # 1
print(max(t))              # 9
print(sum(t))              # 25
print(sorted(t))           # [1, 1, 2, 3, 4, 5, 9] (returns list!)
print(tuple(sorted(t)))    # (1, 1, 2, 3, 4, 5, 9) (back to tuple)

# ============== COMMON PATTERNS ==============
# Return multiple values from function
def get_coordinates():
    return (10, 20)        # Returns tuple

x, y = get_coordinates()   # Unpack directly

# Use as dictionary keys (tuples are hashable, lists are not)
locations = {
    (0, 0): "origin",
    (1, 2): "point A",
    (3, 4): "point B"
}


# ============== WHEN TO USE TUPLES ==============
# ✅ Use tuples when:
# - Data should not change (coordinates, RGB values, database records)
# - Need to use as dictionary key
# - Returning multiple values from function
# - Want to protect data from accidental modification
# - Need slightly better performance than lists

# ❌ Use lists when:
# - Data needs to be modified
# - Need to add/remove elements
# - Order of elements may change