# ============== STRING BASICS ==============
# Strings in Python are immutable sequences of characters
# Can be defined with single, double, or triple quotes

s = "Hello"

# Length
print(len(s))  # 5

# Accessing characters
print(s[0])    # 'H'
print(s[-1])   # 'o'

# Strings are IMMUTABLE - cannot modify in place
# s[0] = 'h'  # TypeError
# Instead, create new string:
new_s = 'h' + s[1:]  # "hello"

# ============== SLICING ==============
s = "Hello, World!"

print(s[0:5])     # "Hello"
print(s[7:])      # "World!"
print(s[:5])      # "Hello"
print(s[-6:])     # "World!"
print(s[:-1])     # "Hello, World"
print(s[::2])     # "Hlo ol!" (every 2nd char)
print(s[::-1])    # "!dlroW ,olleH" (reversed)

# ============== COMMON METHODS ==============
s = "  Hello, World!  "

# Case conversion
print(s.lower())        # "  hello, world!  "
print(s.upper())        # "  HELLO, WORLD!  "

# Whitespace removal
print(s.strip())        # "Hello, World!"
print(s.lstrip())       # "Hello, World!  "
print(s.rstrip())       # "  Hello, World!"

# Search and check
print(s.find("World"))        # 9 (index of first occurrence, -1 if not found)
print(s.count("l"))           # 3
print(s.startswith("  He"))   # True
print(s.endswith("!  "))      # True
print("World" in s)           # True (Pythonic way)

# Replace
print(s.replace("World", "Python"))  # "  Hello, Python!  "

# ============== SPLIT AND JOIN ==============
sentence = "apple,banana,cherry"

# Split string into list
words = sentence.split(",")  # ['apple', 'banana', 'cherry']
# Default split by whitespace: "a b c".split() -> ['a', 'b', 'c']

# Join list into string
joined = ",".join(words)     # "apple,banana,cherry"
joined = " ".join(['a', 'b'])  # "a b"

# Split into lines
multi = "Line1\nLine2\nLine3"
lines = multi.splitlines()   # ['Line1', 'Line2', 'Line3']

# String multiplication
s = "ab" * 3  # "ababab"

# ============== CHARACTER CHECKS ==============
ch = 'A'

print(ch.isalpha())      # True
print(ch.isdigit())      # False
print(ch.isalnum())      # True (alphanumeric)
print(ch.isupper())      # True
print(ch.islower())      # False
print("  ".isspace())    # True

# ============== SORTING ==============
s = "dcba"

# s.sort() # This will raise an AttributeError since strings are immutable and do not have a sort method

sorted_chars = sorted(s)        # ['a', 'b', 'c', 'd'] (returns list)
sorted_str = ''.join(sorted(s)) # "abcd"

# Custom sort
sorted_str = ''.join(sorted(s, reverse=True))  # "dcba"

# ============== ASCII / UNICODE ==============
# ord() - character to ASCII value
print(ord('A'))   # 65
print(ord('a'))   # 97
print(ord('0'))   # 48

# Common patterns
ord('a') - ord('a') # 0 - calculate offset
ord('z') - ord('a')  # 25 - offset from 'a'

# chr() - ASCII value to character
print(chr(65))    # 'A'
print(chr(97))    # 'a'

# ============== STRING FORMATTING ==============
name = "Alice"
age = 30

# f-strings (preferred)
s = f"Name: {name}, Age: {age}"
s = f"Value: {3.14159:.2f}"  # "Value: 3.14" (2 decimal places)

# format() method
s = "Name: {}, Age: {}".format(name, age)

# ============== CONVERSIONS ==============
# String to list of characters
char_list = list("hello")  # ['h', 'e', 'l', 'l', 'o']

# List to string
s = ''.join(['h', 'e', 'l', 'l', 'o'])  # "hello"

# String to int/float
num = int("123")      # 123
num = float("3.14")   # 3.14

# Int to string
s = str(123)          # "123"

# Formatting numbers
num = 3.14159
print(f"{num:.2f}")        # "3.14" - 2 decimal places
print(f"{num:10.2f}")  # "      3.14" - width 10, 2 decimals



# ============== COMMON INTERVIEW PATTERNS ==============

# Check if palindrome helper
s = "racecar"
s == s[::-1]        # True

# Remove non-alphanumeric (for palindrome problems)
s = "A man, a plan, a canal: Panama"
clean = ''.join(c.lower() for c in s if c.isalnum())

# Count character frequency
from collections import Counter
s = "hello"
freq = Counter(s)   # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

# Two pointers on string
s = "hello"
left, right = 0, len(s) - 1
while left < right:
    # do something with s[left] and s[right]
    left += 1
    right -= 1

# Convert list of chars back to string
chars = ['h', 'e', 'l', 'l', 'o']
result = ''.join(chars)     # "hello"

# ============== STRING IMMUTABILITY ==============
# Strings are IMMUTABLE in Python
s = "hello"
# s[0] = 'H'  # TypeError: 'str' object does not support item assignment

# To modify, convert to list first
chars = list(s)     # ['h', 'e', 'l', 'l', 'o']
chars[0] = 'H'      # Now you can modify
s = ''.join(chars)  # "Hello"