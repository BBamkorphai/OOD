class funString():

    def __init__(self, string_input: str):
        self._string_input = string_input

    def __str__(self):
        pass

    def size(self) :
        return len((self._string_input)) 

    def changeSize(self):
        changed_size = []
        for i in self._string_input:
            if i.isupper():
                changed_size.append(chr(ord(i) + 32))
            elif i.islower():
                changed_size.append(chr(ord(i) - 32))
        return "".join(changed_size)


    def reverse(self):
        reversed_input = []
        numstr = len(self._string_input)
        while numstr > 0:
            reversed_input.append(self._string_input[int(numstr) - 1])
            numstr -= 1
        return "".join(reversed_input)

    def deleteSame(self):
        deleted_same = []
        for i in self._string_input:
            if i not in deleted_same:
                deleted_same.append(i)
        return "".join(deleted_same)



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())