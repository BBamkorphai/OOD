print(" ***Function Odd List***")
input_list = (input("Enter list numbers : ")).split()

def transform_to_int(input_number:int):
    original_input_number = []
    for i in input_number:
        original_input_number.append(int(i))
    return original_input_number

def odd_list(input_number:int):
    new_list = []
    for i in input_number:
        if i%2 != 0:
            new_list.append(i)
    return new_list

print("Input list :  {}".format(transform_to_int(input_list)))
print("Output list :  {}".format(odd_list(transform_to_int(input_list))))