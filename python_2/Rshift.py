number, shift = input("Enter number and shiftcount : ").split()

def decimalToBinary(number:int, shift:int):
    binary_number = bin(number).replace("0b", "")
    n = len(binary_number)
    if shift >= 0:
        if shift < n:
            shifted_binary = binary_number[:n-shift]
            result = int(shifted_binary, 2)
        else:
            result = 0
    else:
        shifted_binary = str(int(binary_number)*(10**(shift * -1)))
        result = int(shifted_binary, 2)
    return result


print(decimalToBinary(int(number), int(shift)))
