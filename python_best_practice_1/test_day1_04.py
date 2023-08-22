print("*** String Rotation ***")
words = (input("Enter 2 strings : ")).split()
first_word = words[0]
last_word = words[1]
first_word_list = []
last_word_list = []
count = 0
for i in first_word:
    first_word_list.append(i)
for i in last_word:
    last_word_list.append(i)

def swap_words_last(last_word_list:list):
    last_word_list = last_word_list[3:] + last_word_list[: 3]
    return last_word_list

def swap_words_first(first_word_list:list):
    n = len(first_word_list)
    first_word_list = first_word_list[n-2:] + first_word_list[:n-2]
    return first_word_list


f_current = swap_words_first(first_word_list)
l_current = swap_words_last(last_word_list)

print(str(count + 1) , end=" ")
print(*f_current, sep="" , end=" ")
print(*l_current, sep="")

while first_word_list != f_current or last_word_list != l_current:
    count += 1
    f_current = swap_words_first(f_current)
    l_current = swap_words_last(l_current)

    if count == 5:
        print(" . . . . . ")
    elif count < 5:
        print(str(count + 1) , end=" ")
        print(*f_current, sep="" , end=" ")
        print(*l_current, sep="")
if count > 5:
    print(str(count + 1) , end=" ")
    print(*f_current, sep="" , end=" ")
    print(*l_current, sep="")
print("Total of  {} rounds.".format(count + 1))