nums = [1, 2, 3, 4, 5] # List
nums.append(6) # Adding an element to the list
nums[0] = 10 # Modifying the first element
nums.remove(4) # Removing an element, not the index
print(nums)

del nums[1] # to remove index use del
print(nums)

# index of an element
print("Index of 3 is", nums.index(3))

nums.insert(2, 15) # Inserting 15 at index 2
print(f"after inserting 15 at index 2: {nums}" )


nums.sort() # Sorting the list
print(f"after sorting {nums}" )

nums.reverse
print(f"after reversing {nums}" )

# list can have mixed data types
mixed_list = [1, "hello", 3.14, True]
print(mixed_list)
print(mixed_list[1:3]) # Slicing the list


nums2 = [7, 8, 9,  100, 100, 77, 88, 9]

# min max sum functions
print("Min:", min(nums2), "Max:", max(nums2), "Sum:", sum(nums2))

# Counting occurrences of an element
count_of_88 = nums2.count(88)
print("Count of 88 in nums2:", count_of_88)

# Lists are mutable, so we can change their content 
print("Is 100 in nums2?", 100 in nums2) # Membership test
print("Is 50 in nums2?", 50 in nums2) # Membership test 

print("Concatenated list:", nums + nums2) # Concatenation of lists

# Nested lists
nested_list = [nums, nums2]
print("Nested list:", nested_list)
print("First list in nested list:", nested_list[0])
print("Second list in nested list:", nested_list[1])

# Iterating through a list
for num in nums:
    print("Number:", num)

for i in range(len(nums2)):
    print(f"Index {i}, Value {nums2[i]}")

# Using enumerate to get index and value
for index, value in enumerate(nums2):
    print(f"Index: {index}, Value: {value}")

# List comprehension
squared_nums = [x**2 for x in nums]
print("Squared numbers:", squared_nums)

# Copying a list
copied_list = nums[:]
print("Copied list:", copied_list)

# Clearing a list
nums.clear()
print("Cleared nums list:", nums)

# Extending a list
nums.extend([11, 12, 13])
print("Extended nums list:", nums)

# Slicing with step
print("Every second element in nums2:", nums2[::2])
# Negative indexing
print("Last element in nums2 using negative indexing:", nums2[-1])
print("Second last element in nums2 using negative indexing:", nums2[-2])
print("Slicing nums2 from index 1 to 4:", nums2[1:5])
print("Slicing nums2 from start to index 3:", nums2[:4])
print("Slicing nums2 from index 3 to end:", nums2[3:])

# List unpacking
a, b, c, d, e, f = nums2[:6]
print("Unpacked values:", a, b, c, d, e, f)


# Popping an element from the end
popped_element = nums2.pop()
print("Popped element from nums2:", popped_element)
print("nums2 after popping an element:", nums2)


# Copying a list using the list() constructor
copied_list2 = list(nums2)
print("Copied list using list() constructor:", copied_list2)
# Creating a list using the list() constructor
new_list = list((20, 30, 40))
print("New list created using list() constructor:", new_list)

# Using zip to combine two lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print("Zipped list:", zipped)

# List comprehension with nested loops
combinations = [(x, y) for x in list1 for y in list2]
print("Combinations from list1 and list2:", combinations)
