x = int(input("Enter a Mark out of 100 "))
if x  > 100:
    print("Please enter a Mark out of 100")
elif x >= 90:
    print("You Got a Grade A!")
elif x >= 80:
    print("You got a Grade B")
elif x >= 70:
    print("You got a Grade C")
elif x >= 60:
    print("You got a Grade D")
elif x >= 50:
    print("You Passed!")
else:
    print("You Failed F")

