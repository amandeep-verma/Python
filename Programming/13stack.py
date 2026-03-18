# ============== STACK BASICS ==============
# Stack - Last In First Out (LIFO)
# Best implementation: Python list or collections.deque
# List is sufficient for most cases (append/pop at end are O(1))

# ============== STACK USING LIST (RECOMMENDED) ==============
# List operations at the end are O(1)

stack = []

# Push (add to top) - O(1)
stack.append(1)
stack.append(2)
stack.append(3)
# [1, 2, 3]

# Pop (remove from top) - O(1)
top = stack.pop()           # Returns 3
# [1, 2]

# Peek at top - O(1)
if stack:
    top = stack[-1]         # 2 (doesn't remove)

# Check if empty
is_empty = len(stack) == 0
is_empty = not stack        # Pythonic way

# Size
size = len(stack)

# ============== STACK USING DEQUE ==============
# deque is also efficient, but list is simpler for stacks
from collections import deque

stack = deque()

# Push - O(1)
stack.append(1)
stack.append(2)
stack.append(3)

# Pop - O(1)
top = stack.pop()           # Returns 3

# Peek - O(1)
if stack:
    top = stack[-1]

# ============== STACK OPERATIONS ==============
stack = [1, 2, 3, 4, 5]

# Check membership - O(n)
print(3 in stack)           # True

# Clear stack
stack.clear()               # []

# Iterate through stack (bottom to top)
stack = [1, 2, 3]
for item in stack:
    print(item)             # 1, 2, 3

# Iterate from top to bottom
for i in range(len(stack) - 1, -1, -1):
    print(stack[i])         # 3, 2, 1

# Copy stack
stack_copy = stack[:]
stack_copy = stack.copy()
stack_copy = list(stack)

# ============== STACK CLASS IMPLEMENTATION ==============
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return top item without removing"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items in stack"""
        return len(self.items)
    
    def clear(self):
        """Remove all items"""
        self.items.clear()

# Usage
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())      # 3
print(s.peek())     # 2
print(s.size())     # 2

# ============== COMMON STACK PATTERNS ==============

# Pattern 1: Valid Parentheses
def is_valid_parentheses(s):
    """Check if parentheses are balanced"""
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            # Closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            # Opening bracket
            stack.append(char)
    
    return len(stack) == 0

# Test
print(is_valid_parentheses("()[]{}"))    # True
print(is_valid_parentheses("([)]"))      # False

# Pattern 2: Evaluate Reverse Polish Notation (RPN)
def eval_rpn(tokens):
    """Evaluate postfix expression"""
    stack = []
    
    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # Truncate toward zero
        else:
            stack.append(int(token))
    
    return stack[-1]

# Test
print(eval_rpn(["2", "1", "+", "3", "*"]))  # 9 ((2+1)*3)

# Pattern 3: Next Greater Element
def next_greater_element(nums):
    """Find next greater element for each element"""
    result = [-1] * len(nums)
    stack = []  # Stores indices
    
    for i, num in enumerate(nums):
        # While stack not empty and current > top
        while stack and nums[stack[-1]] < num:
            idx = stack.pop()
            result[idx] = num
        stack.append(i)
    
    return result

# Test
print(next_greater_element([2, 1, 2, 4, 3]))  # [4, 2, 4, -1, -1]

# Pattern 4: Daily Temperatures
def daily_temperatures(temperatures):
    """Days until warmer temperature"""
    result = [0] * len(temperatures)
    stack = []  # Stores indices
    
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    
    return result

# Test
print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# [1, 1, 4, 2, 1, 1, 0, 0]

# Pattern 5: Min Stack (Stack with O(1) min)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Tracks minimum at each level
    
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val
    
    def top(self):
        return self.stack[-1]
    
    def get_min(self):
        return self.min_stack[-1]

# Usage
min_stack = MinStack()
min_stack.push(3)
min_stack.push(5)
min_stack.push(2)
print(min_stack.get_min())  # 2
min_stack.pop()
print(min_stack.get_min())  # 3

# Pattern 6: Monotonic Stack (Increasing)
def monotonic_increasing_stack(nums):
    """Maintains increasing order"""
    stack = []
    
    for num in nums:
        # Remove elements greater than current
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)
    
    return stack

# Test
print(monotonic_increasing_stack([3, 1, 4, 1, 5, 9, 2]))  # [1, 1, 2]

# Pattern 7: Monotonic Stack (Decreasing)
def monotonic_decreasing_stack(nums):
    """Maintains decreasing order"""
    stack = []
    
    for num in nums:
        # Remove elements smaller than current
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)
    
    return stack

# Test
print(monotonic_decreasing_stack([3, 1, 4, 1, 5, 9, 2]))  # [9, 2]

# Pattern 8: Largest Rectangle in Histogram
def largest_rectangle_area(heights):
    """Find largest rectangle in histogram"""
    stack = []  # Stores indices
    max_area = 0
    heights.append(0)  # Sentinel to flush stack
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height_idx = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, heights[height_idx] * width)
        stack.append(i)
    
    heights.pop()  # Remove sentinel
    return max_area

# Pattern 9: Basic Calculator (Infix with +/-)
def calculate(s):
    """Evaluate string expression with +, -, (, )"""
    stack = []
    num = 0
    sign = 1
    result = 0
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            result += sign * num
            num = 0
            sign = 1
        elif char == '-':
            result += sign * num
            num = 0
            sign = -1
        elif char == '(':
            # Push current result and sign to stack
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * num
            num = 0
            result *= stack.pop()  # Pop sign
            result += stack.pop()  # Pop previous result
    
    result += sign * num
    return result

# Test
print(calculate("1 + 1"))           # 2
print(calculate(" 2-1 + 2 "))       # 3
print(calculate("(1+(4+5+2)-3)+(6+8)"))  # 23

# Pattern 10: Remove K Digits
def remove_k_digits(num, k):
    """Remove k digits to make smallest number"""
    stack = []
    
    for digit in num:
        # Remove larger digits
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # Remove remaining k digits from end
    stack = stack[:-k] if k > 0 else stack
    
    # Remove leading zeros and return
    result = ''.join(stack).lstrip('0')
    return result if result else '0'

# Test
print(remove_k_digits("1432219", 3))  # "1219"
print(remove_k_digits("10200", 1))    # "200"

# Pattern 11: Decode String
def decode_string(s):
    """Decode string with pattern k[encoded_string]"""
    stack = []
    current_num = 0
    current_str = ""
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Push current state to stack
            stack.append(current_str)
            stack.append(current_num)
            current_str = ""
            current_num = 0
        elif char == ']':
            # Pop and decode
            num = stack.pop()
            prev_str = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char
    
    return current_str

# Test
print(decode_string("3[a]2[bc]"))      # "aaabcbc"
print(decode_string("3[a2[c]]"))       # "accaccacc"

# Pattern 12: Backspace String Compare
def backspace_compare(s, t):
    """Compare strings with # as backspace"""
    def build(string):
        stack = []
        for char in string:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return ''.join(stack)
    
    return build(s) == build(t)

# Test
print(backspace_compare("ab#c", "ad#c"))  # True
print(backspace_compare("ab##", "c#d#"))  # True

# ============== DFS USING STACK ==============
def dfs_iterative(graph, start):
    """Iterative DFS using stack"""
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node in visited:
            continue
        
        visited.add(node)
        # Process node
        print(node)
        
        # Add neighbors to stack (reverse order for left-to-right)
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

# ============== TIME COMPLEXITY ==============
# Operation         List Stack
# Push              O(1)
# Pop               O(1)
# Peek              O(1)
# Search            O(n)
# Size              O(1)

# ============== BEST PRACTICES ==============
# ✅ Use list for stack in most cases (simple and efficient)
# ✅ Use deque if you need operations at both ends
# ✅ Check if empty before pop/peek to avoid errors
# ✅ Use monotonic stacks for next greater/smaller problems
# ❌ Don't use pop(0) or insert(0, x) - these are O(n)