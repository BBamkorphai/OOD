def hbd(age):
    fake = 21
    base = float((int(age) -1)/2)
    if base%1 != 0:
        base = float((int(age))/2)
        fake = 20
    return "saimai is just {}, in base {}!".format(fake, int(base))

year = input("Enter year : ")

print(hbd(int(year)))