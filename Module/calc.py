

print("hello from calc module. Name is " + __name__)
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def main():
    print("This is a main function inside calc module.")

# This function will only run if this module is executed directly
# But will not run if this module is imported
if __name__ == "__main__":
    main()