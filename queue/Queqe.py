class Queue:
    def __init__(self, list = None):
        if list == None:
            self.queue = []
        else:
            self.queue = list

    def __str__(self) -> str:
        s = ""
        for ele in self.queue:
            s += str(ele)+' '
        return s

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty.")

    def is_empty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queue is empty.")
        


def make_it_easy(input_list:list):
    traned_input = []
    for i in input_list:
        if i == "D":
            traned_input.append(i)
        else:
            a = ''.join(filter(str.isdigit, i))
            traned_input.append(a)
    return traned_input


input_list = input("Enter Input : ").split(",")

Q1 = Queue(make_it_easy(input_list))
Q2 = Queue()
#print(Q1)

for i in range(Q1.size()):
    a = Q1.dequeue()
    if a == "D" and not Q2.is_empty():
        print("{} 0".format(Q2.peek()))
        Q2.dequeue()
    elif a == "D" and Q2.is_empty():
        print("-1")
    else:
        Q2.enqueue(a)
        print(Q2.size())
     
if Q2.is_empty():
    print("Empty")
else:
    print(Q2)
    