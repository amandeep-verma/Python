import calc

# When this module is run directly, __name__ will be "__main__"
# When imported, __name__ will be name of the module
print("hello from learnMain module. Name is " + __name__)

def main():
    print("This is the main function inside learnMain module.")

# Using __name__ to check if this module is being run directly
if __name__ == "__main__":
    main()