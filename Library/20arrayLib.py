import array as arr


# array contains one type of data
# i stands for signed integer
newArr = arr.array('i', [10, 20, 30, 40, 50])

newArr.append(60)  # adding element to the array

newArr.remove(30)  # removing element from the array

newArr.reverse()  # reversing the array

# accessing array elements using index
print("Array elements:")
for i in range(len(newArr)):
    print(newArr[i]) if i == len(newArr) - 1 else print(newArr[i], end=" ")