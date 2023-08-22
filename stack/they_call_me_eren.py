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
    Q1 = Queue()
    Q2 = Queue()
    for i in input_list:
        if i == "D":
            if not Q2.is_empty():
                a = Q2.dequeue()
                print(a)
            elif not Q1.is_empty():
                a = Q1.dequeue()
                print(a)
            else:
                print("Empty")               
        elif 'EN' in i:
            int_input = ''.join(filter(str.isdigit, i))
            Q1.enqueue(int_input)
        elif 'ES' in i:
            int_input = ''.join(filter(str.isdigit, i))
            Q2.enqueue(int_input)

input_list = input("Enter Input : ").split(",")

make_it_easy(input_list)




