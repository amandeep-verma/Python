nums = [1, 2, 3, 4, 5, 10 , 22, 35, 40, 55]

#  the below else works for the for loop, if the loop is not terminated by a break statement.
for num in nums:

    if num % 5 == 0:
        print(f"{num} is divisible by 5")
        break
else:
    print("No number divisible by 5 found in the list.")

