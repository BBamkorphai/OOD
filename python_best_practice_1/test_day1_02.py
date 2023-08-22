print(" *** Divisible number ***")
number = int(input("Enter a positive number : "))

def check_divisible_number(number:int):
    if number <= 0:
        print("0 is OUT of range !!!")
    else:
        list_of_divisible_number = []
        for i in range(1,number+1):
            if number % i == 0:
                list_of_divisible_number.append(i)
        print("Output ==>" ,*list_of_divisible_number)
        print("Total ==> " + str(len(list_of_divisible_number)))

check_divisible_number(number)