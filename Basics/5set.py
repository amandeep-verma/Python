# Sets - hold unique values, unordered. It do not maintains the order of elements
myset = {1, 2, 3, 4, 5, 5, 5, 98, 34, 98}
print(myset) 


if 2 in myset:
    print("2 is present in the set")
# we can not access elements using indexing 
# print(myset[0])  # This will raise a TypeError

#Empty Set
# If we use {} it will create an empty dictionary
emptyset = set()
print("Empty Set:", emptyset)