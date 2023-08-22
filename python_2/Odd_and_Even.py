print("*** Odd Even ***")
input_value = input("Enter Input : ").split(",")

def odd_even(type, data, mode):
    bus = []
    even_bus = []
    result_list = []
    if type == 'S':
        for i in data:
            bus.append(i)
    else:
        bus = data.split()
    for i in range(len(bus)):
        if i%2 != 0:
            even_bus.append(bus[i])
    if Is_odd(mode):
        for i in bus:
            if i not in even_bus:
                result_list.append(i)
    else:
        result_list = even_bus

    if type == "S":
        result = ''.join(result_list)
    else:
        result = result_list

    return result

def Is_odd(mode):
    result = 0
    if mode == "Odd":
        result = 1
    return result

type = input_value[0]
data = input_value[1]
mode = input_value[2]
print(odd_even(type, data, mode))

