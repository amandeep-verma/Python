# ============== QUEUE BASICS ==============
# Queue - First In First Out (FIFO)
# Best implementation: collections.deque - double-ended queue
# Allows insertions/removals from both ends in O(1) time
# Avoid using list.pop(0) - it's O(n)!

from collections import deque

# ============== QUEUE USING DEQUE (RECOMMENDED) ==============
# deque provides O(1) operations at both ends

queue = deque()

# Enqueue (add to back) - O(1)
queue.append(1)
queue.append(2)
queue.append(3)
queue.appendleft(0)  # Add to front if needed
# deque([1, 2, 3])

# Dequeue (remove from front) - O(1)
first = queue.popleft()     # Returns 1
last = queue.pop()         # Returns 3 (from back)
# deque([2, 3])


# Peek at front - O(1)
if queue:
    front = queue[0]        # 2

# Peek at back - O(1)
if queue:
    back = queue[-1]        # 3

# Check if empty
is_empty = len(queue) == 0

# Size
size = len(queue)

# ============== QUEUE OPERATIONS ==============
queue = deque([1, 2, 3, 4, 5])

# Check membership - O(n)
print(3 in queue)           # True

# Clear queue
queue.clear()               # deque([])

# Iterate through queue (doesn't remove elements)
queue = deque([1, 2, 3])
for item in queue:
    print(item)             # 1, 2, 3

# Convert to list
queue_list = list(queue)    # [1, 2, 3]

# ============== QUEUE WITH LIST (NOT RECOMMENDED) ==============
# Using list as queue is INEFFICIENT
# pop(0) is O(n) because all elements need to shift

queue = []

# Enqueue - O(1)
queue.append(1)
queue.append(2)
queue.append(3)

# Dequeue - O(n) ⚠️ SLOW!
first = queue.pop(0)        # Returns 1, but O(n) operation!



# ============== PRIORITY QUEUE ==============
# Elements dequeued in priority order (smallest first)
from queue import PriorityQueue

pq = PriorityQueue()

# Enqueue with priority (lower number = higher priority)
pq.put((2, "task2"))
pq.put((1, "task1"))
pq.put((3, "task3"))

# Dequeue (gets highest priority item)
priority, task = pq.get()   # (1, "task1")
priority, task = pq.get()   # (2, "task2")

# For custom objects, use tuple (priority, item)
# Or implement __lt__ method in your class

# ============== COMMON QUEUE PATTERNS ==============

# Pattern 1: BFS (Breadth-First Search)
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        
        visited.add(node)
        # Process node
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

# Pattern 2: Level Order Traversal (Binary Tree)
def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# Pattern 3: Sliding Window Maximum
from collections import deque

def sliding_window_max(nums, k):
    """Uses deque to track indices of potential maximums"""
    dq = deque()  # Stores indices
    result = []
    
    for i, num in enumerate(nums):
        # Remove indices outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements (they can't be max)
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        # Add to result when window is full
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# Pattern 4: Recent Counter (Fixed Time Window)
from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()
    
    def ping(self, t):
        """Count requests in last 3000ms"""
        self.queue.append(t)
        
        # Remove requests older than 3000ms
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        
        return len(self.queue)

# Pattern 5: Moving Average
from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.sum = 0
    
    def next(self, val):
        self.queue.append(val)
        self.sum += val
        
        if len(self.queue) > self.size:
            removed = self.queue.popleft()
            self.sum -= removed
        
        return self.sum / len(self.queue)

# Pattern 6: Task Scheduler
from collections import deque

def process_tasks():
    """Process tasks in order received"""
    task_queue = deque()
    
    # Add tasks
    task_queue.append("task1")
    task_queue.append("task2")
    task_queue.append("task3")
    
    # Process tasks
    while task_queue:
        task = task_queue.popleft()
        # Process task
        print(f"Processing {task}")

# Pattern 7: Multi-level Cache
from collections import deque

class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = deque()
        self.items = set()
    
    def add(self, item):
        if item in self.items:
            return
        
        if len(self.queue) >= self.capacity:
            removed = self.queue.popleft()
            self.items.remove(removed)
        
        self.queue.append(item)
        self.items.add(item)

# ============== DEQUE AS QUEUE - COMPLETE EXAMPLE ==============
class QueueExample:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        """Add item to back of queue"""
        self.queue.append(item)
    
    def dequeue(self):
        """Remove and return item from front"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.popleft()
    
    def peek(self):
        """Return front item without removing"""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.queue[0]
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self.queue) == 0
    
    def size(self):
        """Return number of items in queue"""
        return len(self.queue)
    
    def clear(self):
        """Remove all items"""
        self.queue.clear()

# Usage
q = QueueExample()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1
print(q.peek())     # 2
print(q.size())     # 2

# ============== CIRCULAR QUEUE ==============
class CircularQueue:
    def __init__(self, k):
        self.queue = [None] * k
        self.size = k
        self.front = 0
        self.rear = -1
        self.count = 0
    
    def enqueue(self, value):
        if self.is_full():
            return False
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.count += 1
        return True
    
    def dequeue(self):
        if self.is_empty():
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True
    
    def front_item(self):
        if self.is_empty():
            return -1
        return self.queue[self.front]
    
    def rear_item(self):
        if self.is_empty():
            return -1
        return self.queue[self.rear]
    
    def is_empty(self):
        return self.count == 0
    
    def is_full(self):
        return self.count == self.size

# ============== TIME COMPLEXITY COMPARISON ==============
# Operation         deque       list        queue.Queue
# Enqueue           O(1)        O(1)        O(1)
# Dequeue           O(1)        O(n) ⚠️     O(1)
# Peek              O(1)        O(1)        N/A
# Size              O(1)        O(1)        O(1)
# Thread-safe       No          No          Yes

# ============== BEST PRACTICES ==============
# ✅ Use deque for single-threaded queue operations
# ✅ Use queue.Queue for multi-threaded applications
# ✅ Use deque with maxlen for sliding windows
# ❌ Don't use list.pop(0) - it's O(n)
# ❌ Don't access middle elements in queue (defeats purpose)