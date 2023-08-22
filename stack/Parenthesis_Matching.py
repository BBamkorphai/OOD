class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
 
class Stack:
 
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]
 
    @property
    def getSize(self):
        return self.size
 
    def isEmpty(self):
        return self.size == 0
 
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
 
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
 
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value
    
stack = Stack()
input_value = input("Enter expresion : ")
input_list = []

for i in input_value:
    stack.push(i)

open_a = 0
close_a = 0
open_b = 0
close_b = 0
open_c = 0
close_c = 0

for i in range(stack.getSize):
    remove = stack.pop()
    if remove == '[':
        open_a += 1
    elif remove == ']':
        close_a += 1
    elif remove == '(':
        open_b += 1
    elif remove == ')':
        close_b += 1
    elif remove == '{':
        open_c += 1
    elif remove == '}':
        close_c += 1

compare_a = open_a - close_a
compare_b = open_b - close_b
compare_c = open_c - close_c
#print(open_a, close_a, open_b, close_b, open_c, close_c)
#print(compare_a, compare_b, compare_c)
if compare_a == 0 and compare_b == 0 and compare_c == 0:
    print("{} MATCH".format(input_value))
elif (compare_a > 0 and close_a == 0 and (close_b != 0 or close_c != 0)) or (compare_b > 0 and close_b == 0 and (close_a != 0 or close_c != 0)) or (compare_c > 0 and close_c == 0 and (close_b != 0 or close_a != 0)):
    print("{} Unmatch open-close".format(input_value))    
elif (compare_a > 0 and close_b == 0 and close_c == 0) or (compare_b > 0 and close_a == 0 and close_c == 0) or (compare_c > 0 and close_a == 0 and close_b == 0):
    if compare_a > 0:
        print("{} open paren excess   {} : {}".format(input_value, compare_a, "["*compare_a))
    if compare_b > 0:
        print("{} open paren excess   {} : {}".format(input_value, compare_b, "("*compare_b))
    if compare_c > 0:
        print("{} open paren excess   {} : {}".format(input_value, compare_c, "{"*compare_c))
elif (compare_a < 0) or (compare_b < 0 ) or (compare_c < 0 ):
    print("{} close paren excess".format(input_value))
