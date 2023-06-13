#Week2
x = int(input("Enter a number 1-7 "))
match x:
    case 1:
        print("Monday",x)
    case 2:
        print("Tuesday",x)
    case 3:
        print("Wednesday",x)
    case 4:
        print("Thursday",x)
    case 5:
        print("Friday",x)
    case 6:
        print("Saturday",x)
    case 7:
        print("Sunday",x)
    case other:
        print("Invalid")
#insted of if..elif..else match..case..case other