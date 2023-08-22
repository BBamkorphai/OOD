class Queue:
    def __init__(self, list = None):
        if list == None:
            self.queue = []
        else:
            self.queue = list

    def __str__(self):
        p = ''
        for ele in self.queue:
            p += str(ele) + ' '
        return p
    
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
        

Q1 = Queue()    
str_input = input("Enter code,hint : ")
for i in str_input:
    Q1.enqueue(i)

differ_change = Q1.size() - 2
change = abs(int(differ_change/10) - int(differ_change%10))
if differ_change/10 > differ_change%10:
    change = (-1) * change

Q2 = Queue()
for i in range(differ_change):
    a = Q1.dequeue()
    secret_code = ord(a)
    secret_code += change
    Q2.enqueue(secret_code)

result_list = []
for i in range(Q2.size()):
    result_list.append(chr(Q2.dequeue()))
    print(result_list)





