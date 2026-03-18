# tuples - are immutable sequences, maintains insertion order. Can store different data types. 
a = (1, 2, 3, 4)
b = ('apple', 'banana', 'cherry')
c = (1, 'apple', 3.14, True)

# Accessing elements
first_element = a[0]  # 1
second_element = b[1]  # 'banana'

# you can not modify a tuple after its creation
# a[0] = 10  # This will raise a TypeError