# ============== LIST BASICS ==============
# Lists are mutable, ordered, and allow duplicates

# Empty list
empty_list = []

# List with n elements (immutable types only: int, str, bool, tuple)
myList = [0] * 5           # [0, 0, 0, 0, 0]
myList = [False] * 3       # [False, False, False]

# ⚠️ DON'T use * with mutable types (list, dict, set)
wrong = [[]] * 3
wrong[0].append(1)         # [[1], [1], [1]] - all sublists changed!

# List with different data types
mixed = [1, "hello", 3.14, True, [1, 2]]

# ============== ACCESSING ELEMENTS ==============
myList = [10, 20, 30, 40, 50]

# Positive indexing (0-based)
print(myList[0])           # 10
print(myList[2])           # 30

# Negative indexing (from end)
print(myList[-1])          # 50
print(myList[-2])          # 40

# ============== SLICING ==============
myList = [10, 20, 30, 40, 50, 60, 70]

print(myList[1:4])         # [20, 30, 40]
print(myList[2:])          # [30, 40, 50, 60, 70]
print(myList[:3])          # [10, 20, 30]
print(myList[::2])         # [10, 30, 50, 70] (every 2nd)
print(myList[1::2])        # [20, 40, 60] (every 2nd from index 1)
print(myList[::-1])        # [70, 60, 50, 40, 30, 20, 10] (reversed)

# Shallow copy
copy_list = myList[:]

# ============== MODIFYING LISTS ==============
myList = [10, 20, 30, 40, 50]

# Add elements
myList.append(60)          # [10, 20, 30, 40, 50, 60] - O(1)
myList.insert(2, 25)       # [10, 20, 25, 30, 40, 50, 60] - O(n)
myList.extend([70, 80])    # [10, 20, 25, 30, 40, 50, 60, 70, 80] - O(k)

# Remove elements
myList.remove(25)          # Removes first occurrence - O(n)
last = myList.pop()        # Removes and returns last element - O(1)
element = myList.pop(2)    # Removes and returns element at index 2 - O(n)
del myList[1]              # Deletes element at index 1 - O(n)
myList.clear()             # Removes all elements - O(n)

# ============== LIST OPERATIONS ==============
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2   # [1, 2, 3, 4, 5, 6]

# Repetition
repeated = list1 * 3       # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# ============== SEARCHING & CHECKING ==============
myList = [10, 20, 30, 40, 50, 30]

# Membership - O(n)
print(30 in myList)        # True
print(100 not in myList)   # True

# Find index - O(n)
index = myList.index(30)   # 2 (first occurrence)

# Count occurrences - O(n)
count = myList.count(30)   # 2

# Length - O(1)
print(len(myList))         # 6

# ============== SORTING & REVERSING ==============
myList = [40, 10, 50, 20, 30]

# sort() - sorts in place, returns None - O(n log n)
myList.sort()              # [10, 20, 30, 40, 50]
myList.sort(reverse=True)  # [50, 40, 30, 20, 10]

# sorted() - returns new sorted list, original unchanged - O(n log n)
original = [40, 10, 50, 20, 30]
sorted_list = sorted(original)  # original unchanged

# Custom sorting with key
words = ["apple", "pie", "a", "cherry"]
words.sort(key=len)        # ['a', 'pie', 'apple', 'cherry']

# Reverse in place - O(n)
myList.reverse()           # reverses the list

# ============== USEFUL BUILT-IN FUNCTIONS ==============
myList = [3, 1, 4, 1, 5, 9, 2, 6]

print(min(myList))         # 1
print(max(myList))         # 9
print(sum(myList))         # 31
print(all(x > 0 for x in myList))  # True (all elements > 0)
print(any(x > 5 for x in myList))  # True (at least one > 5)

# ============== 2D LISTS (MATRICES) ==============
# ❌ WRONG WAY - creates references to same list
wrong_matrix = [[0] * 3] * 2
wrong_matrix[0][0] = 1     # [[1, 0, 0], [1, 0, 0]] - both rows changed!

# ✅ CORRECT WAY - creates independent rows
matrix = [[0] * 3 for _ in range(2)]
matrix[0][0] = 1           # [[1, 0, 0], [0, 0, 0]]

# Accessing 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])        # 6

# ============== COPYING LISTS ==============
original = [1, 2, [3, 4]]

# Shallow copy (nested objects still referenced)
shallow1 = original[:]
shallow2 = original.copy()
shallow3 = list(original)

# Deep copy (for nested structures)
import copy
deep = copy.deepcopy(original)

# ============== COMMON PATTERNS ==============
# Using list as stack (LIFO)
stack = []
stack.append(1)            # push
stack.append(2)
top = stack.pop()          # pop
peek = stack[-1] if stack else None  # peek

# Using list as queue (FIFO) - NOT RECOMMENDED
# Use collections.deque instead (covered in Collections module)
queue = []
queue.append(1)            # enqueue
first = queue.pop(0)       # dequeue - O(n), inefficient!

# ============== COMMON PITFALLS ==============
# ❌ Don't modify list while iterating
# for item in myList:
#     if item == 0:
#         myList.remove(item)  # Can skip elements or cause errors

# ✅ Use list comprehension or iterate over copy
# myList = [item for item in myList if item != 0]
# OR
# for item in myList[:]:
#     if item == 0:
#         myList.remove(item)

# ❌ Don't use mutable default arguments
# def append_to(element, lst=[]):  # BAD! lst persists across calls
#     lst.append(element)
#     return lst

# ✅ Use None as default
# def append_to(element, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(element)
#     return lst