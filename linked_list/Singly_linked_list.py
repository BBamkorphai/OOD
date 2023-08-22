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
        final_str = 'link list : '
        current_node = self.head

        while current_node is not None:
            final_str += str(current_node.data)
            if current_node.next is not None:
                final_str += '->'
            current_node = current_node.next

        if self.size() == 0:
            return "List is empty"

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
            print(f"index = {index} and data = {data}")
        else:
            current_node = self.head
            linked_index = 0
            while linked_index < int(index) - 1:
                current_node = current_node.next
                linked_index += 1
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
            print(f"index = {index} and data = {data}")

link_list = LinkedList()



def to_insert(link_list,i):
    found = 0
    a = ''
    b = ''
    for j in i:
        if j != ':' and found == 0:
            a += str(j)
        elif j == ':':
            found = 1
        elif found == 1 and j != ':':
            b += str(j)
    link_list.insert(a, b)
    print(link_list)

input_list = input("Enter Input : ").split(",")
#print(input_list)
a = ''
first_print = 0
for i in input_list:
    a += str(i) + ' '
preuse_use = a.split(" ")
#print(preuse_use)
ready_to_use = []
for i in preuse_use:
    if i != '':
        ready_to_use.append(i)
#print(ready_to_use)
for i in ready_to_use:
    if ':' not in i:
        link_list.append(i)
    else:
        if first_print == 0:
            if link_list.size() == 0:
                print('List is empty')
            else:
                print(link_list)
            first_print = 1
            to_insert(link_list, i)
        elif link_list.size() == 0:
            #print('List is empty')
            to_insert(link_list, i)
        else:
            to_insert(link_list, i)
        
