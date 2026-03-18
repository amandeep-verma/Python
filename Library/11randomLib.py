import random



# generating a random integer between 1 and 100
random_integer_range = random.randint(1, 100)
print(f"Random integer between 1 and 100: {random_integer_range}")

# generating a random float between 0 and 1
random_float = random.random()
print(f"Random float between 0 and 1: {random_float}")

# generating a random float between a specified range, e.g., 5.0 to 10.0
random_float_range = random.uniform(5.0, 10.0)
print(f"Random float between 5.0 and 10.0: {random_float_range}")
