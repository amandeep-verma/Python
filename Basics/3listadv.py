nums2 = [7, 8, 9,  100, 100, 77, 88, 9]
print("size of the list is", len(nums2)) # Length of the list  

# Custom sorting using a key function
def custom_key(x):
    return x % 10  # Sort based on the last digit   
nums2.sort(key=custom_key)
# can be written as nums2.sort(key=lambda x: x % 10)

print(f"after custom sorting {nums2}" )


# Making another list of indexes of nums2 after sorting based on value
indexes = list(range(len(nums2)))

# Sorting indexes based on corresponding values in nums2, if same value then based on index
indexes.sort(key=lambda i: (nums2[i], i)) # lambda is inline function
print("Indexes after sorting based on nums2 values:", indexes)

# Using filter with a list
filtered_nums = list(filter(lambda x: x > 50, nums2))
print("Filtered nums2 (elements > 50):", filtered_nums)

# Using map with a list
mapped_nums = list(map(lambda x: x * 2, nums2))
print("Mapped nums2 (elements * 2):", mapped_nums)

# Using list as a stack
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack after pushes:", stack)
stack.pop()
print("Stack after pop:", stack)


# Using list as a queue
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue after enqueues:", queue)
queue.popleft()
print("Queue after dequeue:", queue)