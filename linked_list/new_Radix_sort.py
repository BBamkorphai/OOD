class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        final_str = ''
        current_node = self.head

        while current_node is not None:
            final_str += str(current_node.data)
            if current_node.next is not None:
                final_str += ' '
            current_node = current_node.next

        if self.size() == 0:
            return ""

        return final_str

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        r_size = 0
        current_node = self.head
        while current_node is not None:
            r_size += 1
            current_node = current_node.next
        return r_size

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def insert(self, index, data):
        if int(index) < 0 or int(index) > self.size():
            print("Data cannot be added")
        elif int(index) == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            #print(f"index = {index} and data = {data}")
        else:
            current_node = self.head
            linked_index = 0
            while linked_index < int(index) - 1:
                current_node = current_node.next
                linked_index += 1
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
            #print(f"index = {index} and data = {data}")

    def is_in(self, data):
        current_node = self.head
        while current_node is not None:
            if str(current_node) == str(data):
                return True
            current_node = current_node.next
        return False
    
    def find_index(self, data):
        count = 0
        current_node = self.head
        while current_node is not None:
            if str(current_node) == str(data):
                return count
            count += 1
            current_node = current_node.next

    def clear(self):
        self.head = None

    def peek(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current.data if current else None
    
    def delete_target(self, target_data):
        if not self.head:
            return

        if self.head.data == target_data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == target_data:
                current.next = current.next.next
                return
            current = current.next

class LinkedList_type2:
    def __init__(self):
        self.head = None

    def __str__(self):
        final_str = ''
        current_node = self.head

        while current_node is not None:
            final_str += str(current_node.data)
            if current_node.next is not None:
                final_str += ' -> '
            current_node = current_node.next

        # if self.size() == 0:
        #     return "List is empty"

        return final_str

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        r_size = 0
        current_node = self.head
        while current_node is not None:
            r_size += 1
            current_node = current_node.next
        return r_size

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def insert(self, index, data):
        if int(index) < 0 or int(index) > self.size():
            pass
            #print("Data cannot be added")
        elif int(index) == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            #print(f"index = {index} and data = {data}")
        else:
            current_node = self.head
            linked_index = 0
            while linked_index < int(index) - 1:
                current_node = current_node.next
                linked_index += 1
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
            #print(f"index = {index} and data = {data}")

    def delete(self, target_data):
        if not self.head:
            return

        if self.head.data == target_data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == target_data:
                current.next = current.next.next
                return
            current = current.next

    def peek(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current.data if current else None
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
def find_max_digit(data:list):
    max = 0
    for i in data:
        count = 0
        before.append(i)
        for j in i:
            if j.isdigit():
                count += 1
        if count > max:
            max = count
    return max

def is_all_zero(data:list):
    zero = 0
    for i in data:
        if int(i) == 0:
            zero += 1
        if zero == len(data):
            return True
    return False
    

slot = []
while len(slot) < 10:
    a = LinkedList()
    slot.append(a)

#print(slot)

input_list = input("Enter Input : ").split()
round = 1

before = LinkedList_type2()
after = LinkedList_type2() 
all_round = int(find_max_digit(input_list))

if not is_all_zero(input_list):
    while round <= all_round:
        print("------------------------------------------------------------")
        print(f"Round : {round}")
        if round == 1: # first round
            f_count = 0
            current = 0
            for i in range(len(input_list)):
                if str(input_list[i][0]) != '-': # >=0 senario
                    if slot[int(input_list[i][(-1)*round])].head == None: # slot is empty or current
                        slot[int(input_list[i][(-1)*round])].insert(0, input_list[i])
                        current = slot[int(input_list[i][(-1)*round])].head
                        f_count += 1
                    elif slot[int(input_list[i][(-1)*round])].head.data[0] == '-': # current < 0 
                        slot[int(input_list[i][(-1)*round])].insert(0, input_list[i])
                        current = slot[int(input_list[i][(-1)*round])].head
                        f_count += 1
                    else: #slot not empty and current >= 0
                        #print("pass")
                        if current.next == None: #
                            slot[int(input_list[i][(-1)*round])].insert(f_count, input_list[i])
                        f_count += 1
                        current = current.next
                else: # <0 senario
                    #print("pass 2")
                    slot[int(input_list[i][(-1)*round])].append(input_list[i])
            for i in range(len(slot)):
                print(f"{i} : {slot[i]}")
        else: # anothor round
            for i in range(len(slot)):
                slot_size = slot[i].size()
                if not slot[i].isEmpty():
                    for j in range(int(slot_size)):
                        if i == 0:
                            if slot[i].peek(0)[0] != '-': # >=0 senario
                                if len(slot[i].peek(0)) >= round: # have digit senario
                                    if int(slot[i].peek(0)[(-1)*round]) == int(i): #append the same slot
                                        slot[int(slot[i].peek(0)[(-1)*round])].append(slot[i].peek(0))
                                    else: #insert another slot
                                        slot[int(slot[i].peek(0)[(-1)*round])].insert(0, slot[i].peek(0))
                                    slot[i].delete_target(slot[i].peek(0))
                                else: # do not have digit senario
                                    slot[0].append(slot[i].peek(0))
                                    slot[i].delete_target(slot[i].peek(0))
                            else: # <0 senario
                                if len(slot[i].peek(0)) >= round: # have digit senario
                                    if str(slot[i].peek(0)[(-1)*round]) == '-': # fornt is '-'
                                        slot[0].append(slot[i].peek(0))

                                    elif int(slot[i].peek(0)[(-1)*round]) == int(i): #append the same slot
                                        slot[int(slot[i].peek(0)[(-1)*round])].append(slot[i].peek(0))
                                    
                                    else: #insert another slot
                                        slot[int(slot[i].peek(0)[(-1)*round])].append(slot[i].peek(0))
                                    slot[i].delete_target(slot[i].peek(0))
                                else: # do not have digit senario
                                    slot[0].append(slot[i].peek(0))
                                    slot[i].delete_target(slot[i].peek(0))
                        elif slot[i].peek(0)[0] != '-': # >=0 senario
                            if len(slot[i].peek(0)) >= round: # have digit senario
                                if int(slot[i].peek(0)[(-1)*round]) == int(i): #append the same slot
                                    slot[int(slot[i].peek(0)[(-1)*round])].append(slot[i].peek(0))
                                else: #insert another slot
                                    slot[int(slot[i].peek(0)[(-1)*round])].insert(0, slot[i].peek(0))
                                slot[i].delete_target(slot[i].peek(0))
                            else: # do not have digit senario
                                slot[0].insert(0, slot[i].peek(0))
                                slot[i].delete_target(slot[i].peek(0))
                        else: # <0 senario
                            if len(slot[i].peek(0)) >= round: # have digit senario
                                if str(slot[i].peek(0)[(-1)*round]) == '-': # fornt is '-'
                                    slot[0].append(slot[i].peek(0))

                                elif int(slot[i].peek(0)[(-1)*round]) == int(i): #append the same slot
                                    slot[int(slot[i].peek(0)[(-1)*round])].append(slot[i].peek(0))
                                
                                else: #insert another slot
                                    slot[int(slot[i].peek(0)[(-1)*round])].append(slot[i].peek(0))
                                slot[i].delete_target(slot[i].peek(0))
                            else: # do not have digit senario
                                slot[0].append(slot[i].peek(0))
                                slot[i].delete_target(slot[i].peek(0))
            for i in range(len(slot)):
                print(f"{i} : {slot[i]}")
                
        round += 1
    for i in range(len(slot)):
        for j in range(slot[i].size()):
            rent = slot[i].peek(0)
            if str(rent[0]) != '-':
                slot[0].insert(0, rent)
            else:
                slot[0].append(rent)
            slot[i].delete_target(rent)

    while slot[0].head is not None:
        after.append(slot[0].head.data)
        slot[0].delete_target(slot[0].head.data)
    print("------------------------------------------------------------")
    print(f"{round -1} Time(s)")
    print(f"Before Radix Sort : {before}")
    print(f"After  Radix Sort : {after}")
else:
    print("------------------------------------------------------------")
    print("0 Time(s)")
    for i in input_list:
        #before.append(i)
        after.append(i)
    print(f"Before Radix Sort : {before}")
    print(f"After  Radix Sort : {after}")
