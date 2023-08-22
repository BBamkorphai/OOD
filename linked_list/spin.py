
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

        while current_node and current_node.data.isdigit():
            final_str += str(current_node.data)
            if current_node.next is not None:
                final_str += ' <-> '
            current_node = current_node.next

        while current_node and type(current_node.data) == str:
            final_str += str(current_node.data)
            if current_node.next is not None:
                final_str += ' > '
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

    def reverse_till_end(self, index, group):
        prev = None
        current = self.head
        count = 0
        group_count = 0
        next_psudo_head = None
        while group_count < group:
            if group_count == 0:
                psudo_head = current
                while current is not None and count < index:
                    next_node = current.next
                    current.next = prev
                    prev = current
                    current = next_node
                    count += 1
                
                if current:
                    self.head.next = current # connect

                self.head = prev # new head
                count = 0

            elif 0 < group_count < group - 1:
                psudo_head.next = None
                prev = None
                start = current
                while current is not None and count < index:
                    #print(current) # connect
                    next_node = current.next
                    current.next = prev
                    prev = current
                    current = next_node
                    count += 1

                if current:
                    psudo_head.next = prev # connect
                    start.next = current
                # print(psudo_head)
                # print(psudo_head.next)
                # print(start)
                # print(start.next)
                psudo_head = start
                count = 0
            
            elif group_count >= group - 1:
                #print("pass")
                psudo_head.next = None
                prev = None
                prev_current = current
                while current is not None and count < index:
                    #print(current) # connect
                    next_node = current.next
                    current.next = prev
                    prev = current
                    current = next_node
                    count += 1

                
                # print("is pass")
                psudo_head.next = prev # connect
                prev_current.next = current

                count = 0
            # print(group_count)
            group_count += 1
        # print(psudo_head)
        # print(psudo_head.next)
        # print(prev)


# loop circle bug

original = LinkedList()
modified = LinkedList()
input_value = input("Enter the elements of Linked list/group's size: ").split()

for i in input_value:
    if not '/' in i:
        original.append(i)
        modified.append(i)

command = input_value[len(input_value) - 1]
found = 0
a = ''
b = ''

for i in command:
    #print(i)
    if i != '/' and found == 0:
        a += i
        #print("pass a:", a)
    elif i == '/':
        found = 1
        #print("pass found:", found)
    elif found == 1 and i != '/':
        b += i
        #print("pass b:", b)
error = 0
if original.isEmpty():
    print("No elements in Linked List ? OK!")
    error = 1
if int(b) <= 0:
    print("Group' size should be greater than 0")
    error = 1
if error == 0:
    original.append(a)
    modified.append(a)
    print("")
    print(f"Original Linked list: {original}")
    group = (modified.size()/int(b))
    modified.reverse_till_end(int(b), group)
    print(f'Modified Linked list: {modified}')
