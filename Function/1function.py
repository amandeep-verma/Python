def addSubtract(a, b):
    """Returns the sum and difference of two numbers."""
    return a + b, a - b

num1 = 10
num2 = 5
sum_result, diff_result = addSubtract(num1, num2)
print("Sum:", sum_result, "Difference:", diff_result)

# pass by value example
# In Python, immutable types like integers, strings, and tuples are passed by value.
def modify_value(x):
    x += 10
    return x
original_value = 20
modified_value = modify_value(original_value)
print("Original Value:", original_value, "Modified Value:", modified_value)

# pass by reference example
# In Python, mutable types like lists and dictionaries are passed by reference.
def modify_list(lst):
    lst.append(100)

my_list = [1, 2, 3]
modify_list(my_list)
print("Modified List:", my_list)


def person(name, age):
    """Prints the name and age of a person."""
    print("Name:", name)
    print("Age:", age)

# Using keyword arguments to call the function, we can change the order
person(age=30, name="Alice")


def person_info(name, age=25):
    """Prints the name and age of a person with a default age."""
    print("Name:", name)
    print("Age:", age)

person_info("Bob")  # uses default age
person_info("Charlie", 35)  # overrides default age


# variable length arguments
# *args for positional arguments and **kwargs for keyword arguments
def variable_length_args(*args, **kwargs):
    """Prints all positional and keyword arguments."""
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
variable_length_args(1, 2, 3, name="David", age=40)