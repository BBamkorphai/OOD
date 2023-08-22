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

test_linklist = LinkedList()
test_linklist.append(1)
test_linklist.append(2)
test_linklist.append(3)
test_linklist.delete_target(1)
print(test_linklist.peek(0))
print(test_linklist)