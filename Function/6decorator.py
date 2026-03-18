# ============== DECORATOR BASICS ==============
# A decorator is a function that:
# 1. Takes another function as input
# 2. Adds extra functionality (wraps it)
# 3. Returns the enhanced function

# Original function without any modification
def div(a, b):
    return a / b

result1 = div(2, 4)  # Returns 0.5 (2/4)

# ============== CREATING A DECORATOR ==============
# This decorator ensures the larger number is always the numerator
def smart_div(func):
    """Decorator that swaps arguments if a < b before division"""
    def inner(a, b):
        # Add new behavior: swap if needed
        if a < b:
            a, b = b, a
        # Call the original function with (possibly swapped) arguments
        return func(a, b)
    
    # Return the enhanced function
    return inner

# ============== METHOD 1: Using @ Syntax (Most Common) ==============
@smart_div  # Equivalent to: div_decorated = smart_div(div_decorated)
def div_decorated(a, b):
    return a / b

result2 = div_decorated(2, 4)  # Returns 2.0 (4/2 after swap)

# ============== METHOD 2: Manual Decoration ==============
def div2(a, b):
    return a / b

# Manually wrap it with the decorator
div2 = smart_div(div2)  # Now div2() has the swapping behavior

result3 = div2(2, 4)  # Returns 2.0 (4/2 after swap)

# ============== OUTPUT ==============
print("Without decorator:", result1)          # 0.5
print("With @ decorator syntax:", result2)     # 2.0
print("Manual decoration:", result3)           # 2.0