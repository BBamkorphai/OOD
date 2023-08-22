print('*** Fun with permute ***')
input_number = input('input : ')

def transform_to_int(input_number:int):
    input_number = input_number.replace(",", " ")
    input_number = input_number.split()
    original_input_number = []
    for i in input_number:
        original_input_number.append(int(i))
    return original_input_number



def permute(input_number):
    result = [[]]
    for each_num in transform_to_int(input_number):
        bus = []
        for j in result: 
            for k in range(len(j) + 1):
                bus.append(j[:k] + [each_num] + j[k:])
                result = bus
    return result



print("Original Cofllection:  {}".format(transform_to_int(input_number)))
print("Collection of distinct numbers:\n", permute(input_number))
