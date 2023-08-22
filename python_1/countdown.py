print("*** Fun with countdown ***")
input_number = (input("Enter List : ")).split()

def trans_to_int(input_list):
    traned_list = []
    for i in input_list:
        traned_list.append(int(i))
    return traned_list

def countdown(input_number):
    countdown_list = []
    bus = []
    before_number = -10
    for i in input_number:  
        if before_number - i == 1 and before_number not in bus:
            bus.append(before_number)
            bus.append(i)
            if before_number == 2 and i == 1:
                countdown_list.append(bus)
            
        elif before_number - i == 1 and before_number in bus and int(i) == 1:
            bus.append(i)
            countdown_list.append(bus)

        elif before_number - i == 1 and before_number in bus:
            bus.append(i)

        elif before_number - i != 1 and i != 1:
            bus = []

        elif i == 1:
            countdown_list.append([1])
            
        before_number = i

    return countdown_list

def count_list(countdown_list:list):
    counted_list = []
    count = 0
    for i in countdown_list:
        count += 1
    counted_list.append(count)
    counted_list.append(countdown_list)
    return counted_list


print(count_list(countdown(trans_to_int(input_number))))


