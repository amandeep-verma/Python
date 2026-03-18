# ============== ENUMERATE ==============
# enumerate(iterable, start=0) - returns (index, value) pairs

fruits = ['apple', 'banana', 'cherry']

# Basic usage
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# Custom start index
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")
# 1: apple
# 2: banana
# 3: cherry

# Convert to list of tuples
indexed = list(enumerate(fruits))
# [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

# Find indices of matching elements
nums = [10, 20, 30, 20, 40]
indices = [i for i, x in enumerate(nums) if x == 20]
# [1, 3]

# ============== ZIP ==============
# zip(*iterables) - combines multiple iterables into tuples

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['NYC', 'LA', 'Chicago']

# Combine two lists
for name, age in zip(names, ages):
    print(f"{name} is {age}")
# Alice is 25
# Bob is 30
# Charlie is 35

# Combine three lists
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, {city}")

# Convert to list of tuples
pairs = list(zip(names, ages))
# [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Create dictionary from two lists
name_age_dict = dict(zip(names, ages))
# {'Alice': 25, 'Bob': 30, 'Charlie': 35}

# Unzip (transpose)
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, letters = zip(*pairs)
# nums = (1, 2, 3), letters = ('a', 'b', 'c')

# Zip stops at shortest iterable
short = [1, 2]
long = ['a', 'b', 'c', 'd']
result = list(zip(short, long))
# [(1, 'a'), (2, 'b')]

# Parallel iteration over two lists
list1 = [1, 2, 3]
list2 = [10, 20, 30]
result = [x + y for x, y in zip(list1, list2)]
# [11, 22, 33]

# ============== MAP ==============
# map(function, iterable) - applies function to each element

nums = [1, 2, 3, 4, 5]

# Square each number
squared = list(map(lambda x: x**2, nums))
# [1, 4, 9, 16, 25]

# Convert to strings
str_nums = list(map(str, nums))
# ['1', '2', '3', '4', '5']

# With built-in function
floats = ['1.5', '2.3', '3.7']
nums = list(map(float, floats))
# [1.5, 2.3, 3.7]

# Map with multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
result = list(map(lambda x, y: x + y, a, b))
# [11, 22, 33]

# Note: List comprehension is often more Pythonic
squared = [x**2 for x in nums]  # Preferred over map

# ============== FILTER ==============
# filter(function, iterable) - filters elements based on condition

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
# [2, 4, 6, 8, 10]

# Filter numbers > 5
greater = list(filter(lambda x: x > 5, nums))
# [6, 7, 8, 9, 10]

# Filter truthy values (removes 0, None, False, empty strings)
mixed = [0, 1, False, True, '', 'hello', None, 42]
truthy = list(filter(None, mixed))
# [1, True, 'hello', 42]

# Note: List comprehension is often more readable
evens = [x for x in nums if x % 2 == 0]  # Preferred over filter

# ============== ANY ==============
# any(iterable) - returns True if ANY element is truthy

# Check if any number is positive
nums = [-1, -2, 3, -4]
has_positive = any(x > 0 for x in nums)  # True

# Check if any element in list
has_five = any(x == 5 for x in [1, 2, 3, 4, 5])  # True

# Empty iterable
print(any([]))  # False

# All falsy values
print(any([0, False, None, '']))  # False

# At least one truthy
print(any([0, False, 1]))  # True

# ============== ALL ==============
# all(iterable) - returns True if ALL elements are truthy

# Check if all numbers are positive
nums = [1, 2, 3, 4, 5]
all_positive = all(x > 0 for x in nums)  # True

# Check if all even
nums = [2, 4, 6, 8]
all_even = all(x % 2 == 0 for x in nums)  # True

# Empty iterable
print(all([]))  # True (vacuous truth)

# All truthy values
print(all([1, True, 'hello', 42]))  # True

# At least one falsy
print(all([1, True, 0, 42]))  # False

# ============== SUM ==============
# sum(iterable, start=0) - sum of all elements

nums = [1, 2, 3, 4, 5]
total = sum(nums)  # 15

# With start value
total = sum(nums, 10)  # 25 (10 + 15)

# Sum of squares
sum_squares = sum(x**2 for x in nums)  # 55

# Sum specific values
nums = [1, 2, 3, 4, 5, 6]
sum_evens = sum(x for x in nums if x % 2 == 0)  # 12

# Flatten and sum nested list
nested = [[1, 2], [3, 4], [5, 6]]
total = sum(sum(row) for row in nested)  # 21

# ============== LEN ==============
# len(sequence) - length of sequence

print(len([1, 2, 3]))           # 3
print(len("hello"))             # 5
print(len({'a': 1, 'b': 2}))    # 2
print(len({1, 2, 3}))           # 3
print(len((1, 2, 3)))           # 3

# Empty containers
print(len([]))                  # 0
print(len(""))                  # 0

# 2D list - returns number of rows
matrix = [[1, 2, 3], [4, 5, 6]]
print(len(matrix))              # 2
print(len(matrix[0]))           # 3 (columns in first row)

# ============== REVERSED ==============
# reversed(sequence) - returns reverse iterator

nums = [1, 2, 3, 4, 5]

# Iterate in reverse
for num in reversed(nums):
    print(num)  # 5, 4, 3, 2, 1

# Convert to list
rev_list = list(reversed(nums))
# [5, 4, 3, 2, 1]

# Reverse string
s = "hello"
rev_s = ''.join(reversed(s))  # "olleh"

# Note: For lists, [::-1] is also common
rev_list = nums[::-1]  # [5, 4, 3, 2, 1]

# ============== SORTED ==============
# sorted(iterable, key=None, reverse=False) - returns NEW sorted list

nums = [3, 1, 4, 1, 5, 9, 2, 6]

# Basic sorting
sorted_nums = sorted(nums)
# [1, 1, 2, 3, 4, 5, 6, 9]
# Original list unchanged: [3, 1, 4, 1, 5, 9, 2, 6]

# Reverse sort
desc = sorted(nums, reverse=True)
# [9, 6, 5, 4, 3, 2, 1, 1]

# Sort strings
words = ['banana', 'apple', 'cherry']
sorted_words = sorted(words)
# ['apple', 'banana', 'cherry']

# Case-insensitive sort
words = ['banana', 'Apple', 'cherry']
sorted_words = sorted(words, key=str.lower)
# ['Apple', 'banana', 'cherry']

# Sort by length
words = ['apple', 'pie', 'a', 'cherry']
by_length = sorted(words, key=len)
# ['a', 'pie', 'apple', 'cherry']

# Sort by custom function
nums = [-4, -2, 0, 2, 4]
by_abs = sorted(nums, key=abs)
# [0, -2, 2, -4, 4]

# Sort by multiple criteria
students = [('Alice', 25), ('Bob', 20), ('Charlie', 25)]
# Sort by age, then by name
sorted_students = sorted(students, key=lambda x: (x[1], x[0]))
# [('Bob', 20), ('Alice', 25), ('Charlie', 25)]

# Sort dictionary by values
d = {'apple': 3, 'banana': 1, 'cherry': 2}
sorted_items = sorted(d.items(), key=lambda x: x[1])
# [('banana', 1), ('cherry', 2), ('apple', 3)]

# Sort by second element of tuple
pairs = [(1, 5), (3, 2), (2, 8)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
# [(3, 2), (1, 5), (2, 8)]

# ============== SORT (IN-PLACE) ==============
# list.sort(key=None, reverse=False) - sorts list IN PLACE, returns None

nums = [3, 1, 4, 1, 5, 9, 2, 6]

# Basic in-place sort
nums.sort()
# nums is now [1, 1, 2, 3, 4, 5, 6, 9]

# Reverse sort
nums.sort(reverse=True)
# nums is now [9, 6, 5, 4, 3, 2, 1, 1]

# Sort with key function
words = ['apple', 'pie', 'a', 'cherry']
words.sort(key=len)
# words is now ['a', 'pie', 'apple', 'cherry']

# ⚠️ sort() returns None
nums = [3, 1, 4]
result = nums.sort()
# result is None, nums is [1, 3, 4]

# ============== SORT vs SORTED ==============
# sort() - in-place, modifies original list, returns None, only for lists
# sorted() - returns new list, works on any iterable, original unchanged

original = [3, 1, 4, 1, 5]

# Using sort() - modifies original
original.sort()
# original is now [1, 1, 3, 4, 5]

# Using sorted() - original unchanged
original = [3, 1, 4, 1, 5]
new_list = sorted(original)
# original: [3, 1, 4, 1, 5]
# new_list: [1, 1, 3, 4, 5]

# sorted() works on any iterable
sorted_tuple = sorted((3, 1, 4))  # [1, 3, 4] (returns list)
sorted_set = sorted({3, 1, 4})    # [1, 3, 4]
sorted_str = sorted("hello")      # ['e', 'h', 'l', 'l', 'o']

# sort() only works on lists
# (3, 1, 4).sort()  # AttributeError

# ============== CUSTOM SORTING WITH LAMBDA ==============
# Lambda syntax: lambda arguments: expression

# Sort by absolute value
nums = [-4, -2, 0, 2, 4]
sorted(nums, key=lambda x: abs(x))
# [0, -2, 2, -4, 4]

# Sort strings by last character
words = ['apple', 'pie', 'cherry']
sorted(words, key=lambda x: x[-1])
# ['apple', 'pie', 'cherry']

# Sort tuples by second element
pairs = [(1, 5), (3, 2), (2, 8)]
sorted(pairs, key=lambda x: x[1])
# [(3, 2), (1, 5), (2, 8)]

# Sort by multiple criteria (primary: length, secondary: alphabetical)
words = ['apple', 'pie', 'a', 'cherry', 'an']
sorted(words, key=lambda x: (len(x), x))
# ['a', 'an', 'pie', 'apple', 'cherry']

# Sort descending by one criterion, ascending by another
students = [('Alice', 90), ('Bob', 85), ('Charlie', 90)]
sorted(students, key=lambda x: (-x[1], x[0]))
# [('Alice', 90), ('Charlie', 90), ('Bob', 85)]

# Sort by custom function
def custom_key(x):
    return x % 10  # Sort by last digit

nums = [23, 15, 42, 37, 11]
sorted(nums, key=custom_key)
# [11, 42, 23, 15, 37]

# Sort dictionary by key or value
d = {'banana': 3, 'apple': 1, 'cherry': 2}

# By key
sorted(d.items(), key=lambda x: x[0])
# [('apple', 1), ('banana', 3), ('cherry', 2)]

# By value
sorted(d.items(), key=lambda x: x[1])
# [('apple', 1), ('cherry', 2), ('banana', 3)]

# Sort by value descending
sorted(d.items(), key=lambda x: x[1], reverse=True)
# [('banana', 3), ('cherry', 2), ('apple', 1)]

# ============== MIN / MAX ==============
# min/max(iterable, key=None) - return smallest/largest element

# With key function
words = ['apple', 'pie', 'a', 'cherry']
print(min(words, key=len))  # 'a'
print(max(words, key=len))  # 'cherry'

# Min/max by custom criteria
students = [('Alice', 90), ('Bob', 85), ('Charlie', 95)]
print(min(students, key=lambda x: x[1]))  # ('Bob', 85)
print(max(students, key=lambda x: x[1]))  # ('Charlie', 95)


# ============== Bisect module for binary search in sorted lists ==============
import bisect
# Find insertion point to maintain sorted order
sorted_list = [1, 3, 3, 3, 4, 4, 7, 9]
print(bisect.bisect_left(sorted_list, 3))  # 1 (first occurrence of 3)
print(bisect.bisect_right(sorted_list, 3)) # 4 (after last occurrence of 3)
print(bisect.bisect(sorted_list, 3))       # 4 (same as bisect_right)
print(bisect.bisect_left(sorted_list, 5))  # 6 (insertion point for 5)
print(bisect.bisect_right(sorted_list, 5)) # 6 (same as bisect_left for 5)
