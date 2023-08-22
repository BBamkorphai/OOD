import math
class Node:
    def __init__(self, data, next=None, previous=None):
        self.previous = previous
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)
    
class Doubly_likedlist():
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
                previous_node = current_node
            previous_node = current_node
            current_node.next = new_node
            current_node = current_node.next
            current_node.previous = previous_node
        
    def __str__(self):
        final_str = 'link list : '
        current_node = self.head

        while current_node is not None:
            final_str += str(current_node.data)
            if current_node.next is not None:
                final_str += ' -> '
            current_node = current_node.next

        # if self.size() == 0:
        #     return "List is empty"

        return final_str
    
    def size(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count
    
    def revese(self, command:int):
        command_count = 0
        current_node = self.head
        current_node.previous = None
        while current_node is not None:
            if command_count == command - 1:
                pass
            command_count += 1
            current_node = current_node.next



    
original = Doubly_likedlist()
modified = Doubly_likedlist()

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
    if i != '/' and found == 0:
        a += i
    elif i == '/':
        found = 1
    elif found == 1 and i != '/':
        b += i

original.append(a)
modified.append(a)
print(f"Original Linked list: {original}")
group = math.ceil(modified.size()/int(b))
modified.reverse(0 ,int(b))
print(f'Modified Linked list: {modified}')
modified.reverse(int(b), modified.size() - 1)
print(f'Modified Linked list: {modified}')




    