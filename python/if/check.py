c = "y"
while c == "y":
    x = int(input("Enter a number"))
    if x % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
    c = (input("Enter y to continue & enter anything else to exit"))

# % = Gives reminder when we do division
# EXAMPLE # = 4 % 2 = 0