v = int(input("Enter a number"))


def cursion(v):
    if v == 1:
        return v
    print(v, " ",  end = " vihan ")

    cursion(v-1)

cursion(v)