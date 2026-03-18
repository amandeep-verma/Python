# --- METHOD 1: The Module Import ---
import math
# You must use the "math." prefix to access anything inside.
# This is safe because it won't conflict with your own variables.
result1 = math.sqrt(16) 
print(f"Method 1 (math.sqrt): {result1}")


# --- METHOD 2: The Specific Import ---
from math import pi
# Now 'pi' is directly available, but 'sin' or 'cos' are not.
# This is the cleanest way to code.
print(f"Method 2 (pi): {pi}")


# --- METHOD 3: The Wildcard Import ---
from math import *
# Everything (floor, ceil, factorial, etc.) is now in your workspace.
# You don't need prefixes, but you might accidentally overwrite something.
result3 = factorial(5)
print(f"Method 3 (factorial): {result3}")

# ---------------------------------------------------------
# DANGER ZONE: Why Method 3 can be tricky
# ---------------------------------------------------------
# If I create my own function called 'sqrt'...
def sqrt(x):
    return "I am a custom function, not the math one!"

# Now, the 'sqrt' from 'from math import *' is OVERWRITTEN.
print(f"Conflict Example: {sqrt(16)}")