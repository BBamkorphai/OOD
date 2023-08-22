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


zero = LinkedList()
one = LinkedList()
two = LinkedList()
three = LinkedList()
four = LinkedList()
five = LinkedList()
six = LinkedList()
seven = LinkedList()
eight = LinkedList()
nine = LinkedList()

before = LinkedList_type2()
after = LinkedList_type2()

linked_list_store = [zero, one, two, three, four, five, six, seven, eight, nine]

input_value = input("Enter Input : ").split()
max_digit = 0
digit = 0
count_times = 0
zero = 0

is_all_zero = False

for i in input_value:
    before.append(i)
    for j in i:
        if j.isdigit():
            digit += 1
    if digit > max_digit:
        max_digit = digit
    digit = 0
    if int(i) == 0:
        zero += 1
    if zero == len(input_value):
        is_all_zero = True
#print(max_digit)
#test_list = []
print("------------------------------------------------------------")
while count_times != max_digit:
    if count_times > 0:
        for i in range(len(linked_list_store)):
            linked_list_store[i].reverse()
            #print(f"size is : {linked_list_store[i].size()}")
            for j in range(linked_list_store[i].size()):
                rent = linked_list_store[i].peek(0)
                #print(rent)
                linked_list_store[i].delete(rent)
                add = list(rent)
                add.reverse()
                if len(add)-1 >= count_times:
                    if add[count_times] == '-':
                        linked_list_store[0].append(rent)
                    elif int(add[count_times]) > 0:
                        linked_list_store[int(add[count_times])].append(rent)
                elif len(add)-1 < count_times:
                    linked_list_store[0].append(rent)
    else:
        for i in input_value:
            a = list(i)
            #print(a)
            a.reverse()
            if len(a)-1 >= count_times:
                linked_list_store[int(a[count_times])].append(i)
            #print(f"linked_list {int(a[count_times])} is {linked_list_store[int(a[count_times])]}")
            #print(int(a[count_times]))
            #test_list.append(i)
    if not is_all_zero:
        print(f"Round : {count_times + 1}")
        for i in range(len(linked_list_store)):
            linked_list_store[i].reverse()
            print(f"{i} : {linked_list_store[i]}")
        count_times += 1
        print("------------------------------------------------------------")
    else:
        count_times += 1
# for i in linked_list_store:
#     print(i)

#print(test_list)

for i in reversed(range(len(linked_list_store))):
    for j in range(linked_list_store[i].size()):
        rent = linked_list_store[i].peek(0)
        #print(rent)
        linked_list_store[i].delete(rent)
        after.append(rent)

if is_all_zero:
    count_times = 0

print(f"{count_times} Time(s)")
print(f"Before Radix Sort : {before}")
print(f"After  Radix Sort : {after}")

