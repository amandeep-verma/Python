
x = input("Enter something: ")
print("You entered:", x)
print("Type of the input is:", type(x))

y = (int)(x)
print("After converting to integer, type is:", type(y))

z = (int)(input("Enter another number: "))

equation = eval(input("Enter a mathematical expression (e.g., 2 + 3 * 4): "))
print("Result of the expression is:", equation)

# getting element from the argument using agrv
import sys
if len(sys.argv) > 1:
    print("First argument passed from command line is:", sys.argv[1])