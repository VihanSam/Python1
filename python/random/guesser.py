import random
n = random.randint(1, 100)
x = int(input("Guess a number Between 1 to 100"))
v = 0
while x != n:
    v = v + 1
    if x > n:
        print("Number is too High Try Again!")
    if x < n:
        print("Number is too Low Try Again!")
    x = int(input("Guess again!"))
print("Congratulations You WIN!")
print("The number is", n)
print("Number of attempts", v)