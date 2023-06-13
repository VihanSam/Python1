y = int(input("Enter first number"))
s = int(input("Enter second number"))


def greater(x, a):
    if x > a:
        return x
    else:
        return a


g = greater(y, s)
print("The greater number is ", g)
