# heap can store duplicates
# by default heaps are min-heaps in python
import heapq
heap = []
# Each heappush operation takes O(log n) time
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)

# In order to make heapq work as max-heap, we can invert the values
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, (1,2)) # pushing a tuple

# pop elements from min-heap
element = heapq.heappop(heap)  # returns 1
print("Popped from min-heap:", element)


# Using heapify to convert a list into a heap in O(n) time
arr = [7, 2, 6, 3, 9, 1]
heapq.heapify(arr)
print("Heapified array:", arr)


import heapq

# Create an empty list to use as a heap
pq = []

# Add elements (Priority, Task Name)
heapq.heappush(pq, (3, "Low priority task"))
heapq.heappush(pq, (1, "Urgent task"))
heapq.heappush(pq, (2, "Medium task"))

# Pop the task with the highest priority (lowest number)
priority, task = heapq.heappop(pq)
print(f"Processing: {task}")  # Output: Urgent task

# check if priority queue has an element
if 3 in pq:
    print("Task with priority 2 is in the queue")