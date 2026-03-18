# ============== LIST COMPREHENSION ==============
# Syntax: [expression for item in iterable if condition]

# Basic list comprehension
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

# With condition (filter)
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# With if-else (transformation)
parity = ["even" if x % 2 == 0 else "odd" for x in range(5)]
# ['even', 'odd', 'even', 'odd', 'even']

# Transform and filter
squared_evens = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# ============== NESTED LIST COMPREHENSION ==============
# Flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create 2D list
matrix = [[0 for _ in range(3)] for _ in range(2)]
# [[0, 0, 0], [0, 0, 0]]

# Nested with condition
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
# [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

# ============== COMMON LIST COMPREHENSION PATTERNS ==============
# String manipulation
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
# ['HELLO', 'WORLD', 'PYTHON']

# Extract specific characters
text = "hello world"
vowels = [char for char in text if char in "aeiou"]
# ['e', 'o', 'o']

# List of digits from string
num_str = "a1b2c3"
digits = [int(ch) for ch in num_str if ch.isdigit()]
# [1, 2, 3]

# Apply function to each element
nums = [1, 2, 3, 4, 5]
results = [str(x) for x in nums]
# ['1', '2', '3', '4', '5']

# Multiple conditions
nums = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
# [0, 6, 12, 18]
# Equivalent to: if x % 2 == 0 and x % 3 == 0

# Nested if-else
result = [x if x > 0 else 0 if x == 0 else -1 for x in [-2, 0, 3]]
# [-1, 0, 3]

# ============== DICTIONARY COMPREHENSION ==============
# Syntax: {key_expr: value_expr for item in iterable if condition}

# Basic dict comprehension
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# From two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
myDict = {k: v for k, v in zip(keys, values)}
# {'a': 1, 'b': 2, 'c': 3}

# With condition
evens_squared = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}

# Filter dictionary
original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered = {k: v for k, v in original.items() if v > 2}
# {'c': 3, 'd': 4}

# Transform values
prices = {'apple': 2, 'banana': 1, 'orange': 3}
discounted = {k: v * 0.9 for k, v in prices.items()}
# {'apple': 1.8, 'banana': 0.9, 'orange': 2.7}

# Character frequency
text = "hello"
freq = {char: text.count(char) for char in text}
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Better frequency (unique chars only)
freq = {char: text.count(char) for char in set(text)}

# ============== SET COMPREHENSION ==============
# Syntax: {expression for item in iterable if condition}

# Basic set comprehension
squares = {x**2 for x in range(5)}
# {0, 1, 4, 9, 16}

# With condition
evens = {x for x in range(10) if x % 2 == 0}
# {0, 2, 4, 6, 8}

# Unique characters
text = "hello world"
unique_chars = {char for char in text if char.isalpha()}
# {'h', 'e', 'l', 'o', 'w', 'r', 'd'}

# Remove duplicates from list
nums = [1, 2, 2, 3, 3, 4]
unique = {x for x in nums}
# {1, 2, 3, 4}

# ============== TUPLE COMPREHENSION (Generator) ==============
# Note: Parentheses create a generator, not a tuple
# To create tuple, wrap generator in tuple()

# This is a GENERATOR, not tuple
gen = (x**2 for x in range(5))
# <generator object>

# Create tuple from generator
squares_tuple = tuple(x**2 for x in range(5))
# (0, 1, 4, 9, 16)

# ============== GENERATOR EXPRESSIONS ==============
# Similar to list comprehension but with () instead of []
# Generates values on-the-fly, memory efficient for large datasets

# Generator expression
gen = (x**2 for x in range(1000000))  # Doesn't create list in memory

# Use in functions that accept iterables
total = sum(x**2 for x in range(100))  # Memory efficient

# Convert to list when needed
squares_list = list(x**2 for x in range(5))
# [0, 1, 4, 9, 16]

# ============== COMMON INTERVIEW PATTERNS ==============
# Remove non-alphanumeric
s = "A man, a plan, a canal: Panama"
clean = ''.join(c.lower() for c in s if c.isalnum())
# 'amanaplanacanalpanama'

# Matrix transpose
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# [[1, 4], [2, 5], [3, 6]]

# Find indices of target in list
nums = [1, 2, 3, 2, 4, 2]
target = 2
indices = [i for i, x in enumerate(nums) if x == target]
# [1, 3, 5]

# Cartesian product
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
products = [(color, size) for color in colors for size in sizes]
# [('red', 'S'), ('red', 'M'), ('red', 'L'), ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]

# Group elements by property
words = ["apple", "banana", "apricot", "blueberry", "cherry"]
by_first_letter = {word[0]: [w for w in words if w[0] == word[0]] for word in words}
# {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

# Flatten nested list (arbitrary depth - recursive not with comprehension)
# For 2 levels:
nested = [[1, 2], [3, [4, 5]], [6]]
flattened = [item for sublist in nested for item in (sublist if isinstance(sublist, list) else [sublist])]

# ============== WHEN TO USE COMPREHENSIONS ==============
# ✅ Use comprehensions when:
# - Creating new list/dict/set from existing iterable
# - Simple transformation or filtering
# - Code remains readable (< 80 chars, not too nested)

# ❌ Avoid comprehensions when:
# - Logic is complex (use regular for loop)
# - Need to perform side effects (printing, file writing)
# - Multiple statements needed per iteration
# - Comprehension becomes hard to read

# Bad example (too complex)
# result = [x**2 if x > 0 else x**3 if x < 0 else 0 for x in nums if x % 2 == 0 or x % 3 == 0]

# Good example (use regular loop instead)
# result = []
# for x in nums:
#     if x % 2 == 0 or x % 3 == 0:
#         if x > 0:
#             result.append(x**2)
#         elif x < 0:
#             result.append(x**3)
#         else:
#             result.append(0)

# ============== LIST VS GENERATOR ==============
# List comprehension - creates entire list in memory
list_comp = [x**2 for x in range(1000000)]  # Uses ~8MB

# Generator expression - creates values on demand
gen_exp = (x**2 for x in range(1000000))    # Uses minimal memory

# Use generator when:
# - Processing large datasets
# - Only need to iterate once
# - Want memory efficiency

# Example: sum of squares
total = sum(x**2 for x in range(1000000))  # Memory efficient with generator