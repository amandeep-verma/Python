# ============== READING INPUT ==============
# Single line input
line = input()                    # reads entire line as string
line = input().strip()            # removes leading/trailing whitespace

# Single integer
n = int(input())                  # "5" -> 5

# Single float
x = float(input())                # "3.14" -> 3.14

# Multiple integers on same line (space-separated)
a, b, c = map(int, input().split())  # "1 2 3" -> a=1, b=2, c=3

# List of integers from single line
nums = list(map(int, input().split()))  # "1 2 3 4 5" -> [1, 2, 3, 4, 5]

# Multiple values with different types
n, s = input().split()            # "5 hello" -> n="5", s="hello"
n = int(n)                        # convert if needed

# ============== READING MULTIPLE LINES ==============
# Read n lines
n = int(input())
lines = []
for _ in range(n):
    lines.append(input())

# Read n lines of integers
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

# Read until EOF (end of file)
import sys
lines = sys.stdin.readlines()     # returns list of all lines
# OR
lines = [line.strip() for line in sys.stdin]

# ============== READING 2D ARRAY/MATRIX ==============
# Read dimensions then matrix
rows, cols = map(int, input().split())
matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Alternative: list comprehension
rows, cols = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]

# ============== PRINTING OUTPUT ==============
# Basic print
print("Hello")                    # Hello
print(42)                         # 42

# Print multiple values (space-separated by default)
print(1, 2, 3)                    # 1 2 3

# Print without newline
print("Hello", end="")            # Hello (no newline)
print("World")                    # HelloWorld

# Custom separator
print(1, 2, 3, sep=", ")          # 1, 2, 3
print(1, 2, 3, sep="-")           # 1-2-3

# Print list/array elements
nums = [1, 2, 3, 4, 5]
print(*nums)                      # 1 2 3 4 5 (unpacks list)
print(" ".join(map(str, nums)))   # 1 2 3 4 5

# ============== FORMATTED OUTPUT ==============
# f-strings (Python 3.6+)
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")  # Name: Alice, Age: 25

# Decimal places
pi = 3.14159
print(f"{pi:.2f}")                # 3.14
print(f"{pi:.4f}")                # 3.1416

# Width and alignment
num = 42
print(f"{num:5d}")                # "   42" (right-aligned, width 5)
print(f"{num:05d}")               # "00042" (zero-padded)

# ============== PRINTING 2D ARRAY/MATRIX ==============
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Print each row on new line
for row in matrix:
    print(*row)
# Output:
# 1 2 3
# 4 5 6
# 7 8 9

# Print with custom separator
for row in matrix:
    print(" ".join(map(str, row)))

# ============== COMMON INPUT PATTERNS ==============
# Test cases: First line is T (number of test cases)
t = int(input())
for _ in range(t):
    # Process each test case
    n = int(input())
    # ... solve problem

# Grid/Matrix input as strings
n = int(input())
grid = []
for _ in range(n):
    grid.append(input())  # each row as string
# grid[i][j] to access character at row i, col j

# Parse comma-separated values
line = input()                    # "1,2,3,4,5"
nums = list(map(int, line.split(',')))  # [1, 2, 3, 4, 5]

# ============== FAST I/O (for competitive programming) ==============
import sys
input = sys.stdin.readline        # faster input

# Fast output (use sparingly, print is usually fine)
sys.stdout.write(str(result) + '\n')

# ============== READING FROM FILE (for local testing) ==============
# Read from file
with open('input.txt', 'r') as f:
    lines = f.readlines()
    # OR
    for line in f:
        pass
        # process line


# Write to file
with open('output.txt', 'w') as f:
    f.write("Result: " + str(result) + '\n')

# ============== ERROR HANDLING ==============
# Handle invalid input
try:
    n = int(input())
except ValueError:
    print("Invalid input")
    n = 0

# ============== USEFUL CONVERSIONS ==============
# String to list of characters
s = "hello"
chars = list(s)                   # ['h', 'e', 'l', 'l', 'o']

# String to list of integers (digits)
s = "12345"
digits = [int(d) for d in s]     # [1, 2, 3, 4, 5]

# List to string
chars = ['h', 'e', 'l', 'l', 'o']
s = ''.join(chars)                # "hello"

# Integer list to string
nums = [1, 2, 3, 4, 5]
s = ''.join(map(str, nums))       # "12345"