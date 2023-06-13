def evenOrOdd(x):
    if x % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd") 
c = "y"
while c == "y":
    x = int(input("Enter a number"))
    evenOrOdd(x)
    c = (input("Enter y to continue & enter anything else to exit"))