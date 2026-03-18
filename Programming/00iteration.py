# ============== RANGE BASICS ==============
# range(stop) -> 0 to stop-1
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# range(start, stop) -> start to stop-1
for i in range(2, 7):  # 2, 3, 4, 5, 6
    print(i)

# range(start, stop, step)
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i)

# Negative step for reverse iteration
for i in range(10, 0, -1):  # 10, 9, 8, ..., 1
    print(i)

# Converting range to list
range_list = list(range(5))
print("Range as list:", range_list)

# ============== LIST ITERATION PATTERNS ==============
myList = [10, 20, 30, 40, 50]

# Pattern 1: Index-based iteration (when you need index)
for i in range(len(myList)):
    print(f"Index: {i}, Value: {myList[i]}")

# Pattern 2: Reverse iteration using range
for i in range(len(myList) - 1, -1, -1):
    print(f"Index: {i}, Value: {myList[i]}")

# Pattern 3: enumerate (PREFERRED when you need both index and value)
for i, v in enumerate(myList):
    print(f"Index: {i}, Value: {v}")

for i, v in enumerate(myList, start=2):  # starts counting from 2
    print(f"Index: {i}, Value: {v}")

for i, v in enumerate(reversed(myList)):  # enumerate with reversed
    print(f"Index: {i}, Value: {v}")

# Pattern 4: Direct iteration (when you only need values)
for value in myList:
    print(f"Value: {value}")

# Pattern 5: Reverse iteration using reversed() - more Pythonic
for value in reversed(myList):
    print(f"Value: {value}")

# ============== LEETCODE-SPECIFIC PATTERNS ==============

# Two pointers from both ends
left, right = 0, len(myList) - 1
while left < right:
    print(f"Left: {myList[left]}, Right: {myList[right]}")
    left += 1
    right -= 1

# Sliding window with range
window_size = 3
for i in range(len(myList) - window_size + 1):
    window = myList[i:i + window_size]
    print(f"Window starting at {i}: {window}")