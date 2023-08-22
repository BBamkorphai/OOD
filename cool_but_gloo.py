import random
import math

print("*** Fun with permute ***")
input_number = (input("input : "))

def transform_to_int(input_number:int):
    input_number = input_number.replace(",", " ")
    input_number = input_number.split()
    original_input_number = []
    for i in input_number:
        original_input_number.append(int(i))
    return original_input_number

def permute(input_list:list):
    print(random.randint(0, 10))

def count_the_same(input_list):
    same_list = []
    for i in input_list:
        count = 0
        for j in input_list:
            if i == j:
                count += 1
        same_list.append(count)
        while i in input_list:
            input_list.remove(i)
    return same_list

def find_possibly(input_list:list, same_list:list):
    under = 0
    for i in same_list:
        under += math.factorial(i)
    return math.factorial(len(input_list))/under



print("Original Cofllection:  {}".format(transform_to_int(input_number)))
print("the same : {}".format(count_the_same(transform_to_int(input_number))))
print("possibility : {}".format(find_possibly( transform_to_int(input_number) ,count_the_same(transform_to_int(input_number)))))
#print("print the same {}".format(count_the_same(transform_to_int(input_number))))
""" print("Collection of distinct numbers:")
print(permute(transform_to_int(input_number))) """