from numpy import *

arr1 = array([1, 2, 3, 4, 5])
arr2 = array([10,11,12,13,14])
arr3 = array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print("Array 1:", arr1+5) # vector addition
print("Array 2:", arr2*2) # scalar multiplication
print("Element-wise addition:", arr1 + arr2) # element-wise addition

# Using numpy function sum
print("sum of arr1:", sum(arr1))


arrCopy = arr1.copy() # creates a deep copy
arrView = arr1.view() # creates a shallow copy

print("dimensions of arr3:", arr3.ndim)
print("shape of arr3:", arr3.shape)
print("size of arr3:", arr3.size)
print("data type of arr3:", arr3.dtype)

arrFlattened = arr3.flatten()
print("Flattened arr3:", arrFlattened)

arrTwoDim = arr3.reshape(3, 4) # reshaping to D2 array
print("Reshaped arr3 to 3x4:\n", arrTwoDim)

arrThreeDim = arr3.reshape(2, 2, 3) # reshaping to D3 array
print("Reshaped arr3 to 2x2x3:\n", arrThreeDim)

# Matrix Operations
# m = matrix('1 2 3; 4 5 6; 7 8 9') # creating matrix from string
m = matrix(arr3)
print("Matrix m:\n", m)

print("Transpose of m:\n", m.T)

print("diagonal of m:", m.diagonal())

print('minimum element in m:', m.min())

# multiplication of two matrices
m1 = matrix('1 2 3; 3 4 5')
m2 = matrix('5 6; 7 8; 9 10')
mProduct = m1 * m2
print("Product of m1 and m2:\n", mProduct)