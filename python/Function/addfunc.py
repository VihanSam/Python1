# Def  =  function
def add(x, y):
    print(x, " + ", y, " = ", x + y)


def subtract(x, y):
    print(x, " - ", y, " = ", x - y)


def divide(x, y):
    print(x, " / ", y, " = ", x / y)


def multiply(x, y):
    print(x, " * ", y, " = ", x * y)


x = int(input("Enter first number!"))
y = int(input("Enter second number!"))
add(x, y)
subtract(x, y)
divide(x, y)
multiply(x, y)
