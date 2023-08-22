class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self) -> str:
        s = "Stack of " + str(self.size()) + " items : "
        for ele in self.items:
            s += str(ele)+' '
        return s
    
    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == [] # return checking condition
    
    def size(self):
        return len(self.items)
    
    @property
    def my_items(self):
        return self.items
    
s1 = Stack()
s2 = Stack()

inp = input('Enter Input : ').split(',')

walking_history = []
for i in inp:
    if i == "B":
        walking_history.append(i)
    else:
        int_input = ''.join(filter(str.isdigit, i))
        walking_history.append(int_input)

for i in walking_history:
    s1.push(i)

while not s1.isEmpty():
    tree = s1.pop()
    s2.push(tree)

countable_tree = []
before_tree = 10000
filtered_list = []

while not s2.isEmpty():
    if not s2.peek().isalpha():
        if int(s2.peek()) < int(before_tree):
            current_tree = s2.pop()
            before_tree = current_tree
            countable_tree.append(current_tree)
        else:
            current_tree = s2.pop()
            for i in countable_tree:
                if int(i) > int(current_tree):
                    filtered_list.append(i)
            countable_tree = filtered_list
            countable_tree.append(current_tree)
            before_tree = current_tree
            filtered_list = []
    else:
        print(len(countable_tree))
        s2.pop()
