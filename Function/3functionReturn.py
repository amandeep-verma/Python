# input is 1 list and return is 2 lists
def segeragate(numbers):
    even = []
    odd = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

lst = [20,25,14, 19, 16, 24, 47, 52, 31]

even, odd = segeragate(lst)

print("Even numbers:", even, "Odd numbers:", odd)