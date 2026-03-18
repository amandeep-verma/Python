# ============== LIST BASICS ==============
# Lists in Python can hold elements of different data types
# Lists are mutable, ordered, and allow duplicates
# Can be used as arrays, stacks, queues, etc.

# Empty list
empty_list = []
print("Empty list:", empty_list)

# List with n elements initialized to default value of immmutable types - int, str, bool, tuple
myList = [0] * 5
print("List with default values:", myList)  # [0, 0, 0, 0, 0]

myList = [False] * 3
print("List with False values:", myList)  # [False, False, False]

# don't try to create list with mutable types like list, dict, set, custom objects using * operator
# as they will create references to same object
# For example:
wrong_list = [[]] * 3
wrong_list[0].append(1)
print("Wrong list (mutable types):", wrong_list)  # [[1], [1], [1]] - all sublists changed!

# List with different data types
mixed_list = [1, "hello", 3.14, True, [1, 2]]
print("Mixed list:", mixed_list) # [1, 'hello', 3.14, True, [1, 2]]

print("5th element of mixed list:", mixed_list[4])  # [1, 2]

# List from range
myList = list(range(1, 6))
print("List from range:", myList)  # [1, 2, 3, 4, 5]

# ============== ACCESSING ELEMENTS ==============
myList = [10, 20, 30, 40, 50]

# Positive indexing (0-based)
print("First element:", myList[0])  # 10
print("Third element:", myList[2])  # 30

# Negative indexing (from end)
print("Last element:", myList[-1])  # 50
print("Second to last:", myList[-2])  # 40

# ============== SLICING ==============
myList = [10, 20, 30, 40, 50, 60, 70]

# list[start:stop] -> start to stop-1
print(myList[1:4])  # [20, 30, 40]

# list[start:] -> start to end
print(myList[2:])  # [30, 40, 50, 60, 70]

# list[:stop] -> beginning to stop-1
print(myList[:3])  # [10, 20, 30]

# list[start:stop:step]
print(myList[::2])  # [10, 30, 50, 70] (every 2nd element)
print(myList[1::2])  # [20, 40, 60] (every 2nd starting from index 1)

# Reverse a list using slicing
print(myList[::-1])  # [70, 60, 50, 40, 30, 20, 10]

# Shallow copy using slicing
copy_list = myList[:]
print("Shallow copy:", copy_list)

# ============== MODIFYING LISTS ==============
myList = [10, 20, 30, 40, 50]

# Append (add to end) - O(1)
myList.append(60)
print("After append:", myList)  # [10, 20, 30, 40, 50, 60]

# Insert at specific index - O(n)
myList.insert(2, 25)
print("After insert:", myList)  # [10, 20, 25, 30, 40, 50, 60]

# Extend (add multiple elements) - O(k) where k is length of iterable
myList.extend([70, 80])
print("After extend:", myList)  # [10, 20, 25, 30, 40, 50, 60, 70, 80]

# Remove by value (first occurrence) - O(n)
myList.remove(25)
print("After remove:", myList)  # [10, 20, 30, 40, 50, 60, 70, 80]

# Pop (remove and return last element) - O(1)
last = myList.pop()
print("Popped element:", last)  # 80
print("After pop:", myList)  # [10, 20, 30, 40, 50, 60, 70]

# Pop at specific index - O(n)
element = myList.pop(2)
print("Popped element at index 2:", element)  # 30
print("After pop at index:", myList)  # [10, 20, 40, 50, 60, 70]

# Delete by index - O(n)
del myList[1]
print("After del:", myList)  # [10, 40, 50, 60, 70]

# Clear all elements - O(n)
temp_list = [1, 2, 3]
temp_list.clear()
print("After clear:", temp_list)  # []

# ============== LIST OPERATIONS ==============
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print("Concatenated:", combined)  # [1, 2, 3, 4, 5, 6]

# Repetition
repeated = list1 * 3
print("Repeated:", repeated)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# ============== SEARCHING & CHECKING ==============
myList = [10, 20, 30, 40, 50, 30]

# Check if element exists - O(n)
print("30 in list:", 30 in myList)  # True
print("100 not in list:", 100 not in myList)  # True

# Find index of first occurrence - O(n)
index = myList.index(30)
print("Index of 30:", index)  # 2

# Count occurrences - O(n)
count = myList.count(30)
print("Count of 30:", count)  # 2

# Length of list - O(1)
print("Length:", len(myList))  # 6

# ============== SORTING ==============
myList = [40, 10, 50, 20, 30]

# Sort in place - O(n log n)
myList.sort() # .sort()  returns None, It is an in-place sorting
print("Sorted ascending:", myList)  # [10, 20, 30, 40, 50]

myList.sort(reverse=True)
print("Sorted descending:", myList)  # [50, 40, 30, 20, 10]

# Sorted (returns new list, original unchanged) - O(n log n)
original = [40, 10, 50, 20, 30]
sorted_list = sorted(original)
print("Original:", original)  # [40, 10, 50, 20, 30]
print("Sorted copy:", sorted_list)  # [10, 20, 30, 40, 50]

# Custom sorting with key
words = ["apple", "pie", "a", "cherry"]
words.sort(key=len)
print("Sorted by length:", words)  # ['a', 'pie', 'apple', 'cherry']

# Custom sorted with key
original = ["apple", "pie", "a", "cherry"]
sorted_list = sorted(original, key= len)
print("Original:", original)  # ['apple', 'pie', 'a', 'cherry']
print("Sorted by length copy:", sorted_list)  # ['a', 'pie', 'apple', 'cherry']

# Reverse in place - O(n)
myList.reverse()
print("Reversed:", myList)  # [10, 20, 30, 40, 50]

# ============== LIST COMPREHENSION ==============
# Basic list comprehension
squares = [x**2 for x in range(5)]
print("Squares:", squares)  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print("Evens:", evens)  # [0, 2, 4, 6, 8]

# With if-else
parity = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print("Parity:", parity)  # ['even', 'odd', 'even', 'odd', 'even']

# Nested comprehension (flatten 2D list)
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print("Flattened:", flattened)  # [1, 2, 3, 4, 5, 6]

# ============== COMMON LEETCODE PATTERNS ==============

# Two pointers
def two_pointers_example(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Process arr[left] and arr[right]
        left += 1
        right -= 1

# Sliding window
def sliding_window_example(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# Using list as stack (LIFO)
stack = []
stack.append(1)  # push
stack.append(2)
top = stack.pop()  # pop
peek = stack[-1] if stack else None  # peek

# Using list as queue (FIFO) - NOT RECOMMENDED, use collections.deque instead
# But if needed:
queue = []
queue.append(1)  # enqueue
queue.append(2)
first = queue.pop(0)  # dequeue - O(n), inefficient!

# ============== 2D LISTS (MATRICES) ==============
# ⚠️ WRONG WAY - creates references to same list
wrong_matrix = [[0] * 3] * 2
wrong_matrix[0][0] = 1
print("Wrong matrix:", wrong_matrix)  # [[1, 0, 0], [1, 0, 0]] - both rows changed!

# ✅ CORRECT WAY - creates independent rows
correct_matrix = [[0] * 3 for _ in range(2)]
correct_matrix[0][0] = 1
print("Correct matrix:", correct_matrix)  # [[1, 0, 0], [0, 0, 0]]

# Accessing 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Element at [1][2]:", matrix[1][2])  # 6

# ============== USEFUL BUILT-IN FUNCTIONS ==============
myList = [3, 1, 4, 1, 5, 9, 2, 6]

print("Min:", min(myList))  # 1
print("Max:", max(myList))  # 9
print("Sum:", sum(myList))  # 31
print("All positive:", all(x > 0 for x in myList))  # True
print("Any > 5:", any(x > 5 for x in myList))  # True

# ============== COPYING LISTS ==============
original = [1, 2, [3, 4]]

# Shallow copy (nested objects are still referenced)
shallow1 = original[:]
shallow2 = original.copy()
shallow3 = list(original)

# Deep copy (for nested structures)
import copy
deep = copy.deepcopy(original)


# Custom sorting

# ============== COMMON PITFALLS ==============
# ❌ Don't modify list while iterating
# for item in myList:
#     if item == 0:
#         myList.remove(item)  # Can cause issues

# ✅ Use list comprehension instead
# myList = [item for item in myList if item != 0]

# ❌ Don't use mutable default arguments
# def append_to(element, lst=[]):  # BAD!
#     lst.append(element)
#     return lst

# ✅ Use None as default
# def append_to(element, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(element)
#     return lst