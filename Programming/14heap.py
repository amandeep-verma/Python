# ============== HEAP BASICS ==============
# Heap - Binary tree where parent <= children (min-heap) or parent >= children (max-heap)
# Python's heapq implements MIN-HEAP by default
# Time: Push O(log n), Pop O(log n), Peek O(1), Heapify O(n)

import heapq

# ============== MIN-HEAP OPERATIONS ==============
# Create empty heap
min_heap = []

# Push elements - O(log n)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 7)
heapq.heappush(min_heap, 2)
# min_heap = [1, 2, 3, 7, 5]

# Pop smallest element - O(log n)
smallest = heapq.heappop(min_heap)  # Returns 1
# min_heap = [2, 5, 3, 7]

# Peek at smallest (without removing) - O(1)
if min_heap:
    smallest = min_heap[0]          # 2

# Size - O(1)
size = len(min_heap)

# Check if empty
is_empty = len(min_heap) == 0

# ============== HEAPIFY - CONVERT LIST TO HEAP ==============
# Heapify existing list - O(n) [more efficient than n pushes]
arr = [7, 2, 6, 3, 9, 1]
heapq.heapify(arr)
# arr is now a valid heap: [1, 2, 6, 3, 9, 7]

# Note: heapify modifies list in-place, doesn't return anything
# After heapify, arr[0] is always the minimum

# ============== MAX-HEAP (NEGATE VALUES) ==============
# Python only has min-heap, so negate values for max-heap
max_heap = []

# Push (negate values)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -3)
# max_heap = [-5, -1, -3]

# Pop largest (negate back)
largest = -heapq.heappop(max_heap)  # Returns 5 (not -5)

# Peek at largest
if max_heap:
    largest = -max_heap[0]           # 3

# Heapify for max-heap
arr = [7, 2, 6, 3, 9, 1]
arr = [-x for x in arr]              # Negate all
heapq.heapify(arr)
# To get values back: [-x for x in arr]

# ============== HEAP WITH TUPLES (PRIORITY QUEUE) ==============
# Tuples compared element-by-element
pq = []

# Push (priority, value)
heapq.heappush(pq, (3, "Low priority"))
heapq.heappush(pq, (1, "High priority"))
heapq.heappush(pq, (2, "Medium priority"))

# Pop highest priority (lowest number)
priority, task = heapq.heappop(pq)   # (1, "High priority")

# With tie-breaking (priority, secondary_sort, value)
heapq.heappush(pq, (1, 0, "Task A"))
heapq.heappush(pq, (1, 1, "Task B"))  # Same priority, different secondary
priority, secondary, task = heapq.heappop(pq)  # (1, 0, "Task A")

# ============== HEAP WITH Dictionary ==============
# Use (priority, key) and store values in separate dict
pq = []
tasks = {"task1": 3, "task2": 1, "task3": 2}
for task, priority in tasks.items():
    heapq.heappush(pq, (priority, task))
# Pop highest priority task
priority, task = heapq.heappop(pq)  # (1, "task2")  


# ============== HEAP WITH CUSTOM OBJECTS ==============
# Use tuple with sort key first
class Task:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name

pq = []
task1 = Task(3, "Low")
task2 = Task(1, "High")

# Push tuple (priority, task)
heapq.heappush(pq, (task1.priority, task1))
heapq.heappush(pq, (task2.priority, task2))

priority, task = heapq.heappop(pq)
print(task.name)  # "High"

# Alternative: Use counter for tie-breaking with unhashable objects
from itertools import count
counter = count()
pq = []
heapq.heappush(pq, (1, next(counter), task1))
heapq.heappush(pq, (1, next(counter), task2))

# ============== ADVANCED HEAP FUNCTIONS ==============

# heappushpop - push then pop (more efficient than separate operations)
heap = [1, 3, 5, 7]
result = heapq.heappushpop(heap, 2)  # Push 2, then pop min
# result = 1, heap = [2, 3, 5, 7]

# heapreplace - pop then push (more efficient than separate operations)
heap = [1, 3, 5, 7]
result = heapq.heapreplace(heap, 2)  # Pop min, then push 2
# result = 1, heap = [2, 3, 5, 7]

# nlargest - get n largest elements - O(n log k)
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
largest_3 = heapq.nlargest(3, nums)
# [42, 37, 23]

# nsmallest - get n smallest elements - O(n log k)
smallest_3 = heapq.nsmallest(3, nums)
# [-4, 1, 2]

# With key function
words = ['apple', 'pie', 'a', 'cherry']
longest_2 = heapq.nlargest(2, words, key=len)
# ['cherry', 'apple']

# ============== COMMON HEAP PATTERNS ==============

# Pattern 1: Kth Largest Element
def find_kth_largest(nums, k):
    """Find kth largest element using min-heap of size k"""
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

# Test
print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5

# Pattern 2: Top K Frequent Elements
from collections import Counter
def top_k_frequent(nums, k):
    """Find k most frequent elements"""
    count = Counter(nums)
    # Use negative frequency for max-heap behavior
    return [num for num, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])]

# Test
print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]

# Pattern 3: Merge K Sorted Lists
def merge_k_sorted_lists(lists):
    """Merge k sorted lists using min-heap"""
    heap = []
    result = []
    
    # Initialize heap with first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))  # (value, list_idx, element_idx)
    
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    
    return result

# Test
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
print(merge_k_sorted_lists(lists))  # [1, 1, 2, 3, 4, 4, 5, 6]

# Pattern 4: K Closest Points to Origin
def k_closest_points(points, k):
    """Find k points closest to origin"""
    # Use max-heap of size k (negate distances)
    heap = []
    for x, y in points:
        dist = -(x*x + y*y)  # Negative for max-heap
        if len(heap) < k:
            heapq.heappush(heap, (dist, [x, y]))
        else:
            heapq.heappushpop(heap, (dist, [x, y]))
    
    return [point for _, point in heap]

# Test
print(k_closest_points([[1, 3], [-2, 2], [5, 8], [0, 1]], 2))
# [[0, 1], [-2, 2]] or [[-2, 2], [0, 1]]

# Pattern 5: Median from Data Stream
class MedianFinder:
    def __init__(self):
        self.small = []  # Max-heap (negate values)
        self.large = []  # Min-heap
    
    def add_num(self, num):
        # Add to max-heap (small)
        heapq.heappush(self.small, -num)
        
        # Balance: move largest from small to large
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Maintain size property (small.size >= large.size)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
    
    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0

# Usage
mf = MedianFinder()
mf.add_num(1)
mf.add_num(2)
print(mf.find_median())  # 1.5
mf.add_num(3)
print(mf.find_median())  # 2.0

# Pattern 6: Task Scheduler (with cooldown)
from collections import Counter
def least_interval(tasks, n):
    """Find minimum intervals needed with cooldown n"""
    count = Counter(tasks)
    max_heap = [-cnt for cnt in count.values()]
    heapq.heapify(max_heap)
    
    time = 0
    while max_heap:
        temp = []
        for _ in range(n + 1):
            if max_heap:
                temp.append(heapq.heappop(max_heap))
        
        for cnt in temp:
            if cnt + 1 < 0:  # Still has tasks remaining
                heapq.heappush(max_heap, cnt + 1)
        
        time += (n + 1) if max_heap else len(temp)
    
    return time

# Pattern 7: Sliding Window Median
def median_sliding_window(nums, k):
    """Find median of each sliding window"""
    from sortedcontainers import SortedList
    window = SortedList(nums[:k])
    medians = []
    
    for i in range(k, len(nums) + 1):
        # Get median
        if k % 2 == 0:
            medians.append((window[k//2 - 1] + window[k//2]) / 2)
        else:
            medians.append(window[k//2])
        
        if i < len(nums):
            # Slide window
            window.remove(nums[i - k])
            window.add(nums[i])
    
    return medians

# Pattern 8: Ugly Number II
def nth_ugly_number(n):
    """Find nth ugly number (factors only 2, 3, 5)"""
    heap = [1]
    seen = {1}
    
    for _ in range(n):
        num = heapq.heappop(heap)
        for factor in [2, 3, 5]:
            new_num = num * factor
            if new_num not in seen:
                seen.add(new_num)
                heapq.heappush(heap, new_num)
    
    return num

# Test
print(nth_ugly_number(10))  # 12

# ============== CHECKING MEMBERSHIP ==============
# Check if element exists - O(n)
heap = [1, 3, 5, 7, 9]
if 3 in heap:
    print("3 is in heap")

# Note: This is O(n) linear search
# For O(1) membership, maintain separate set

# ============== HEAP WITH SET FOR FAST LOOKUP ==============
class HeapWithSet:
    def __init__(self):
        self.heap = []
        self.items = set()
    
    def push(self, item):
        if item not in self.items:
            heapq.heappush(self.heap, item)
            self.items.add(item)
    
    def pop(self):
        item = heapq.heappop(self.heap)
        self.items.remove(item)
        return item
    
    def __contains__(self, item):
        return item in self.items

# ============== HEAP PROPERTIES ==============
# - Always balanced (complete binary tree)
# - Parent index: (i-1)//2
# - Left child: 2*i+1
# - Right child: 2*i+2
# - Root (min/max) always at index 0

# ============== TIME COMPLEXITY ==============
# Operation         Time
# Push              O(log n)
# Pop               O(log n)
# Peek              O(1)
# Heapify           O(n)
# Search            O(n)
# nlargest/nsmallest O(n log k)

# ============== BEST PRACTICES ==============
# ✅ Use heapq for priority queue
# ✅ Negate values for max-heap
# ✅ Use tuples for priority queue with values
# ✅ Use heapify for bulk operations (faster than multiple pushes)
# ✅ Use nlargest/nsmallest for finding top k
# ❌ Don't use for random access (use array/list instead)
# ❌ Don't modify heap array directly (breaks heap property)