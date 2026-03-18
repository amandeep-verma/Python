class Computer:

    def config(self):
        print("i5, 16GB, 1TB")


com1 = Computer()
print(type(com1))

# we can also call a method inside a class without creating an object by directly calling the class name and method name
Computer.config(com1)

# Mostly we use object to call the method. But this is to say that we are passing com1 as self argument to the method
com1.config()