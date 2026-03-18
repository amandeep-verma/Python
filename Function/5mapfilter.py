
nums = [2,4,3,5,6,7,8,9,10 ]

def isEven(n):
    return n % 2 == 0

# Filter takes 2 arguments: function and iterable
evens = list(filter(isEven, nums))
print("Even numbers:", evens)

# Using lambda function to filter odd numbers
odds = list(filter(lambda x: x % 2 != 0, nums))
print("Odd numbers:", odds)

# Map takes 2 arguments: function and iterable
# Using lambda function to double the odd numbers
doubles = list(map(lambda x: x*2, odds))
print("Doubled odd numbers:", doubles)

# Need to import reduce from functools module
from functools import reduce

# Using lambda function to sum the doubled odd numbers
# reduce takes 2 arguments: function and iterable
sum = reduce(lambda x, y: x + y, doubles)
print("Sum of doubled odd numbers:", sum)