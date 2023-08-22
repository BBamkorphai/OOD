n, s = input("Enter n, s: ").split()
holding_list = []
# holding_list = [1,2,3,4,5]

def format_print(holding_list, count = 0, out_str = ''):
    if count <= len(holding_list) - 1:
        out_str += str(holding_list[count])
        count += 1
        if count < len(holding_list):
            out_str += ' + '
        format_print(holding_list, count, out_str)
    else:    
        print(out_str)

def find_max_split(original, head):
    if int(original) - int(head) <= head:
        return int(original) - int(head)
    else:
        return int(head)
    
def clear_list(holding_list):
    pass

def is_done_check(holding_list, n, count=0):
    if count <= len(holding_list) - 1:
        if holding_list[count] != 1 and count == 0:
            count += 1
            return is_done_check(holding_list, n, count)
            
        elif holding_list[count] != 1 and count != 0:
            return False
        
        elif holding_list[count] == 1 and count != 0:
            count += 1
            return is_done_check(holding_list, n, count)
        
        elif holding_list[count] == 1 and count == 0:  
            return True 
    else:
        return True 
    
def find_not_one_index(holding_list, count=0):
    if count <= len(holding_list) - 2:
        if holding_list[count] != 1 and holding_list[count + 1] == 1:
            return count
        else:
            count += 1
            return find_not_one_index(holding_list, count)
    else:
        return count
    
# Enter n, s: 6 8
# 6
# 5 + 1
# 4 + 2
# 4 + 1 + 1
# 3 + 3
# 3 + 2 + 1
# 3 + 1 + 1 + 1
# 2 + 2 + 2

def partition(n, s, holding_list, count = 1):   
    if holding_list[0] != 1:
        #print(count)
        if is_done_check(holding_list, len(holding_list), count = 0):
            if len(holding_list) == 1:
                holding_list[0] -= 1
                holding_list.append(1)
                #print("pass1")
                #if  count < int(s):
                format_print(holding_list)
                count += 1
                partition(n, s, holding_list, count)
            else:
                # here
                sum_all = sum(holding_list)
                head = holding_list[0] - 1
                if head >= sum_all - head:
                    tail = sum_all - head
                    holding_list = []
                    holding_list.append(head)
                    holding_list.append(tail)
                    #print("pass2")
                    #if  count < int(s):
                    format_print(holding_list)
                    count += 1
                    partition(n, s, holding_list, count)
                else:
                    #print("----------------------------------------------------------------")
                    #print("pass3")
                    sum_all = sum(holding_list)
                    head = holding_list[0] - 1
                    times = int(sum_all/head)
                    #print(f"times = {times}")
                    holding_list = []
                    holding_list.append(head)
                    holding_list = holding_list * times
                    #print(holding_list)
                    second_sum = sum(holding_list)
                    if second_sum != sum_all:
                        add = sum_all - second_sum
                        holding_list.append(add)
                        #if  count < int(s):
                        format_print(holding_list)
                        count += 1
                        partition(n, s, holding_list, count)
                    else:
                        #if  count < int(s):
                        format_print(holding_list)
                        count += 1
                        partition(n, s, holding_list, count)
        else:
            #print(holding_list)
            #print(find_not_one_index(holding_list))
            holding_list[find_not_one_index(holding_list)] -= 1
            holding_list.append(1)
            #print("pass4")
            #if  count < int(s):
            format_print(holding_list)
            count += 1
            partition(n, s, holding_list, count)
    else:
        if count > int(s):
            print(". . .")
        print(f"Total: {count}")

if int(n) == 0:
    print("0")
    print("Total: 1")
else:
    holding_list.append(int(n))
    if int(s) != 0:
        format_print(holding_list)
    partition(n, s, holding_list)