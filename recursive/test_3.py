def find_not_one_index(holding_list, count=0):
    if count <= len(holding_list) - 2:  # Adjusted the upper limit to avoid index out of range
        if holding_list[count] != 1 and holding_list[count + 1] == 1:
            return count
        else:
            count += 1
            return find_not_one_index(holding_list, count)  # Added "return" here
    else:
        return count  # Return None if the condition is not met

holding_list = [7, 3]
print(find_not_one_index(holding_list))