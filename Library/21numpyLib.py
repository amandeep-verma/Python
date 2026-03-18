import numpy
# numply allows to use multi dimesional array which is not a feature from array package

twoDimList = [[1,2,4],[5,6,7],[8,9,10]]

# Using numpy functions
print("NumPy array mean:", numpy.sum(twoDimList))
print("NumPy array mean:", numpy.mean(twoDimList))

# Numpy array don't need the type to be defined, although you can define it if needed
twoDimArray = numpy.array([[1,2,4],[5,6,7],[8,9,10]])

# Using built in functions of numpy
print("Sum:",twoDimArray.sum())
print("NumPy array mean:", twoDimArray.max)

# You can create numpy array with mixed types, it will upcast to the most general type
newArr = numpy.array([1,2,4,5,6.0])
print("type is", newArr.dtype)

newArr2 = numpy.linspace(1,10,5) # from range 1 to 10, creates 5 elements
print("linspace:", newArr2)

numArr3 = numpy.arange(1,10,2) # from range 1 to 10, step by 2
print("arange:", numArr3)

numArr4 = numpy.logspace(1,10,5) # from range 1 to 10, creates 5 elements in log scale
print("logspace:", numArr4)

numArr5 = numpy.zeros((3,4)) # creates a 3x4 array with all elements as zero
print("zeros:", numArr5)

numArr6 = numpy.ones((3,4), int) # creates a 3x4 array with all elements as one of type int
print("ones:", numArr6)