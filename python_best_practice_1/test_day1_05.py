class MyInt:
    def __init__(self, num) -> None:
        self._num = num
        self._list_of_roman = []
        self._original_num = num

    @property
    def num(self):
        return self._num
    
    @property
    def list_of_roman(self):
        return self._list_of_roman
    
    @property
    def original_num(self):
        return self._original_num
    
    def toRoman(self):
        while float(self._num)/1000 >= 1:
            self._list_of_roman.append("M")
            self._num -= 1000

        if float(self._num)/100 >= 9:
            self._list_of_roman.append("CM")
            self._num -= 900

        if 5 > float(self._num)/100 >= 4:
            self._list_of_roman.append("CD")
            self._num -= 400

        while float(self._num)/500 >= 1:
            self._list_of_roman.append("D")
            self._num -= 500

        while float(self._num)/100 >= 1:
            self._list_of_roman.append("C")
            self._num -= 100

        if float(self._num)/10 >= 9:
            self._list_of_roman.append("XC")
            self._num -= 90

        if 5 > float(self._num)/10 >= 4:
            self._list_of_roman.append("XL")
            self._num -= 40

        while float(self._num)/50 >= 1:
            self._list_of_roman.append("L")
            self._num -= 50

        while float(self._num)/10 >= 1:
            self._list_of_roman.append("X")
            self._num -= 10

        if float(self._num) == 9:
            self._list_of_roman.append("IX")
            self._num -= 9

        if 5 > float(self._num) == 4:
            self._list_of_roman.append("IV")
            self._num -= 4

        while float(self._num) >= 5:
            self._list_of_roman.append("V")
            self._num -= 5

        while float(self._num) >= 1:
            self._list_of_roman.append("I")
            self._num -= 1

        if None in self._list_of_roman:
            self._list_of_roman.remove(None)

        print("{} convert to Roman : ".format(self._original_num), end='')
        print(*self._list_of_roman, sep='')

        return 

print(" *** class MyInt ***")
all_num = (input("Enter 2 number : ")).split()
a = MyInt(int(all_num[0]))
b = MyInt(int(all_num[1]))
a.toRoman()
b.toRoman()
f_result = int(all_num[0]) + int(all_num[1])
f_result = f_result + (f_result/2)
print("{} + {} = {}".format(all_num[0], all_num[1], int(f_result)))