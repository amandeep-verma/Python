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