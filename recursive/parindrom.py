input_value = input("Enter Input : ")
original = input_value
def is_palindrome(input_value):
    if input_value != "":
        if input_value[0] == input_value[-1]:
            input_value = input_value[1:-1]
            is_palindrome(input_value)
        else:
            print(f"'{original}' is not palindrome")
    else:
        print(f"'{original}' is palindrome")

is_palindrome(input_value)
