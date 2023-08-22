print(" *** String count ***")
words = (input("Enter message : "))

def check_upper(word):
    count = 0
    upper_list = []
    for i in words:
        if i.isupper() == True:
            count+=1
            if i not in upper_list:
                upper_list.append(i)
    print("No. of Upper case characters : " + str(count))
    upper_list.sort()
    print("Unique Upper case characters : ", end = "")
    print(*upper_list, sep = "  ")

def check_lower(word):
    count = 0
    lower_list = []
    for i in words:
        if i.islower() == True:
            count+=1
            if i not in lower_list:
                lower_list.append(i)
    print("No. of Lower case Characters : " + str(count))
    lower_list.sort()
    print("Unique Lower case characters : ", end = "")
    print(*lower_list, sep = "  ")

check_upper(words)
check_lower(words)