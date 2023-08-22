def is_done_check(holding_list, n, count=0):
    if count <= len(holding_list) - 1:
        if holding_list[count] != 1 and count == 0:
            count += 1
            #print("pass2")
            return is_done_check(holding_list, n, count)  # Return the result of the recursive call
            
        elif holding_list[count] != 1 and count != 0:
            #print("pass3")
            return False  # Return False instead of "False"
        elif holding_list[count] == 1 and count != 0:
            #print("pass4")
            count += 1
            return is_done_check(holding_list, n, count)  # Return the result of the recursive call
        elif holding_list[count] == 1 and count == 0:  
            return True 
    else:
        return True  # Return True instead of "True"

holding_list = [7]
print(is_done_check(holding_list, len(holding_list)))