a = 10

# demonstrating use of global keyword
def func():
    global a
    a += 5
    print("Inside func, a =", a)

func()
print("Outside func, a =", a)


b = 20

# demonstrating use of globals() to modify global variable and local variable with same name
def func2():
    b = 40
    x = globals()
    x['b'] += 10  # modifies the global variable b
    print("Inside func2, b =", b)
func2()

print("Outside outer_func, b =", b)