# ============== BASIC ARITHMETIC ==============
a, b = 10, 3

# Division types
print(10 / 3)     # 3.3333... (float division)
print(10 // 3)    # 3 (floor division - rounds down)
print(-10 // 3)   # -4 (rounds down toward negative infinity)
print(10 ** 3)    # 1000 (power/exponent)
print(10 % 3)     # 1 (modulo - remainder)

# Note that in Python, modulo of negative numbers can yield a positive result, which is different from some other languages.
import math
print(math.fmod(-10, 3))   # -1.0 (modulo with sign of dividend)

# Absolute value
print(abs(-5))    # 5
print(abs(5))     # 5

# ============== MIN/MAX ==============
# With two values
print(min(5, 10))        # 5
print(max(5, 10))        # 10

# With multiple values
print(min(5, 10, 3, 8))  # 3
print(max(5, 10, 3, 8))  # 10

# With iterables
nums = [5, 10, 3, 8]
print(min(nums))         # 3
print(max(nums))         # 10

# ============== ROUNDING ==============
x = 3.7
y = 3.2

print(round(3.7))        # 4
print(round(3.2))        # 3
print(round(3.14159, 2)) # 3.14 (round to 2 decimal places)

# Banker's rounding (rounds to nearest even number)
print(round(3.5))        # 4 (rounds to nearest even)
print(round(2.5))        # 2 (rounds to nearest even)


# Floor and ceiling
import math
print(math.floor(3.7))   # 3 (rounds down)
print(math.ceil(3.2))    # 4 (rounds up)

# ============== COMMON MATH FUNCTIONS ==============
import math

# Power and roots
print(pow(2, 3))         # 8 (same as 2 ** 3)
print(math.sqrt(16))     # 4.0 (square root)
print(16 ** 0.5)         # 4.0 (alternative square root)
print(8 ** (1/3))        # 2.0 (cube root)

# Logarithms
print(math.log(8, 2))    # 3.0 (log base 2 of 8)
print(math.log10(100))   # 2.0 (log base 10)
print(math.log(2.718))   # 1.0 (natural log, base e)

# Constants
print(math.pi)           # 3.141592653589793
print(math.e)            # 2.718281828459045

# ============== INTEGER OPERATIONS ==============
# Check even/odd
n = 10
is_even = n % 2 == 0     # True
is_odd = n % 2 == 1      # True

# Get sign of number
def sign(n):
    if n > 0: return 1
    elif n < 0: return -1
    else: return 0

# Swap two numbers
a, b = 5, 10
a, b = b, a              # a=10, b=5

# Sum of digits
n = 1234
digit_sum = sum(int(d) for d in str(n))  # 10

# ============== COMMON PATTERNS ==============
# GCD (Greatest Common Divisor)
import math
print(math.gcd(48, 18))  # 6

# LCM (Least Common Multiple)
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Check if power of 2
n = 16
is_power_of_2 = (n > 0) and (n & (n - 1)) == 0  # True

# Check if prime (simple approach)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# ============== MODULO TRICKS ==============
# Modulo to keep number in range
n = 15
print(n % 10)            # 5 (keeps single digit)

# Negative modulo (watch out!)
print(-1 % 5)            # 4 (not -1)
print(-7 % 3)            # 2

# Circular array indexing
arr = [1, 2, 3, 4, 5]
i = 7
print(arr[i % len(arr)]) # arr[2] = 3

# ============== INFINITY ==============
# Useful for initialization
pos_inf = float('inf')
neg_inf = float('-inf')

print(pos_inf > 1000000) # True
print(neg_inf < -1000000) # True

# Comparing with infinity
nums = [1, 2, 3]
min_val = float('inf')
for n in nums:
    min_val = min(min_val, n)

# ============== DIVISION CEILING TRICK ==============
# Ceiling division without importing math
a, b = 10, 3
ceil_div = (a + b - 1) // b  # 4
# OR
ceil_div = -(-a // b)         # 4

# ============== SUM AND PRODUCT ==============
nums = [1, 2, 3, 4, 5]

# Sum
total = sum(nums)        # 15

# Product (no built-in, use loop or math.prod in Python 3.8+)
import math
product = math.prod(nums)  # 120

# Manual product
product = 1
for n in nums:
    product *= n

# ============== RANDOM (for testing) ==============
import random

# Random integer in range [a, b] inclusive
random.randint(1, 10)    # e.g., 7

# Random float in range [0, 1)
random.random()          # e.g., 0.342

# Random choice from list
nums = [1, 2, 3, 4, 5]
random.choice(nums)      # e.g., 3

# Shuffle list in-place
random.shuffle(nums)