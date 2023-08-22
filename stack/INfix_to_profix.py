class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self) -> str:
        s = "Stack of " + str(self.size()) + " items :"
        for ele in self.items:
            s += str(ele)+''
        return s
    
    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
def Infix_to_Profix(str_input:str):
    operator_list = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    s = Stack()
    output = ""
    for i in str_input:
        if i.isalnum():
            output += i
        elif i == '(':
            s.push(i)
        elif i == ')':
            while s.size() != 0 and s.peek() != '(':
                next_op = s.pop()
                output += next_op
            s.pop()
        elif i in operator_list:
            while (s.size() != 0 and s.peek() != '(' and operator_list[i] <= operator_list[s.peek()]):
                next_op = s.pop()
                output += next_op
            s.push(i)

    while not s.isEmpty():
        output += s.pop()

    return output

input_str = input("Enter Infix : ")
print("Postfix : {}".format(Infix_to_Profix(input_str)))