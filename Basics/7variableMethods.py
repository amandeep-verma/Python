value = None # we use None to represent null value
print("Initial value:", value)

a =5
b= 5
c = a
print("address of a:", id(a))
print("address of b:", id(b))
print("address of c:", id(c))
# Above all three variables point to same memory location

# type of variable
print("type of a:", type(a))
someArray = [1,2,3]
print("type of arrays:", type(someArray))

num = 1.2345
print("type of num:", type(num))

numInInt = int(num)
print("numInInt:", numInInt)
print("type of numInInt:", type(numInInt))