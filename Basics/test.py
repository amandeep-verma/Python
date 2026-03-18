newList = [1, 2, 3, 4, 5]

copyList  = newList

print("Original List:", id(newList))
print("Copied List:", id(copyList))

secondCopy = newList[:]
print("Second Copied List:", id(secondCopy))

secondCopy.append(6)

print("newList before modification:", newList)
print("copyList before modification:", secondCopy)


myset = {}
myset.add(1)
myset.add(2)
print("Set contents:", myset)