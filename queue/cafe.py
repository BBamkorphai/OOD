class Queue:
    def __init__(self, list=None):
        if list is None:
            self.queue =[]
        else:
            self.queue = list
    
    def __str__(self):
        s = ''
        for ele in self.queue:
            s += str(ele) + ' '
        return s
    
    def enqueue(self, item):
        return self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            raise IndexError('Queue is empty')

    def isEmpty(self):
        return self.queue == []
    
    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            raise IndexError('Queue is empty')
        
    def size(self):
        return len(self.queue)
        
class customer:
    def __init__(self,arrive_time):
        self.arrive = arrive_time
        self.waitng_time = 0
        self.status = 'waiting'
        self.time = 0

    def time_to_drink(self):
        self.status = 'drinking'

    def decrease_time(self):
        self.time -= 1

    def show_status(self):
        return self.status

class barista:
    def __init__(self):
        self.status = 'free'
        self.time = 0
        self.finished_time = 0
        self.done_cof = 0
        self.customer_num = -99

    def brewing(self, order_time):
        self.finished_time += int(order_time)
        self.status = 'brewing'

    def decrease_time(self):
        self.time -= 1

    def now_free(self):
        self.status = 'free'

    def Just_done(self):
        self.status = 'Just done'

    def show_status(self):
        return self.status
    
    def is_finished_time(self):
        return self.finished_time == self.time
    
    def show_done_cof(self):
        return self.done_cof
    
    def time_now(self):
        return self.time
    
    def finish_coffee(self):
        self.done_cof += 1

    def counting(self):
        if self.status == 'brewing':
            self.time += 1
        #self.finished_time += 1

    def customer_queue(self, queue):
        self.customer_num = queue

    def show_queue(self):
        return str(int(self.customer_num)+1)

print(" ***Cafe***")
input_value = input("Log : ").split("/")
#print(input_value)
ordering_time = []
for i in input_value:
    ordering_time.append(i.split(","))

print(ordering_time)

for i in range(len(ordering_time)):
    ordering_time[i].append(i)
print(ordering_time)

Q1 = Queue(ordering_time)
B1 = barista()
B2 = barista()
bill_history = []
bus = []
wait_history = []
time = 0
waiting_time = 0
""" print(not Q1.isEmpty())
print(B1.show_status())
print(B2.show_status())
"""

while not Q1.isEmpty() or B1.show_status() == 'brewing' or B2.show_status() == 'brewing':
    print("pass loop : {}".format(time))
    if bus == []:
        for i in range(Q1.size()):
            a = Q1.peek()
            if (bus == [] or bus[0][0] == a[0]) and int(a[0]) <= time:
                b = Q1.dequeue()
                bus.append(b)

    print(int(a[0]))
    print(time)
    print("bus : {}".format(bus))
    

    if B1.show_status() == 'brewing' and B2.show_status() == 'brewing' and bus != []:
        if int(bus[0][0]) <= time:
            print("active")
            waiting_time += 1

    if B1.is_finished_time() and B1.show_status() == 'brewing':
        B1.Just_done()
        B1.finish_coffee()

    if B2.is_finished_time() and B2.show_status() == 'brewing':
        B2.Just_done()
        B2.finish_coffee()

    if B1.show_status() == 'Just done' and B1.show_done_cof() != 0:
        #print("B1 DONE")
        B1.now_free()
        bill_history.append(B1.show_queue())
        #print("Time {} customer {} get coffee".format(time, B1.show_queue()))
    
    #print(B2.show_done_cof())
    if B2.show_status() == 'Just done' and B2.show_done_cof() != 0:
        #print("B2 DONE")
        B2.now_free()
        bill_history.append(B2.show_queue())
        #print("Time {} customer {} get coffee".format(time, B2.show_queue()))

    

    # elif (B1.show_status() == 'free' or B2.show_status() == 'free') and int(a[0]) <= time:
    #     a.append(waiting_time)
    #     wait_history.append(a)
    #     waiting_time = 0

    outing_queue = bill_history
    outing_queue.sort()
    for i in outing_queue:
        print("Time {} customer {} get coffee".format(time, i))
    outing_queue = []
    bill_history = []


    #print("bus : {}".format(bus))
    #print("Q1 : {}".format(Q1))

    if (B1.show_status() == 'free' or B2.show_status() == 'free') and bus != []:
        if B1.show_status() == 'free':
            if bus != []:
                B1.brewing(bus[0][1])
                B1.customer_queue(bus[0][2])
                bus.pop(0)
                #print("B1 brewing type 1")
                #print(B1.show_status())
                #print(bus)

        #print(bus)
        if B2.show_status() == 'free' and B1.show_status() == "brewing" and bus != []:
            #print("pass this con")
            if bus != []:
                B2.brewing(bus[0][1])
                B2.customer_queue(bus[0][2])
                bus.pop(0)
                #print("B2 brewing type 1")
        #print(bus)

    #print(B1.show_status())
    #print(B2.show_status())
    

    time += 1
    B1.counting()
    B2.counting()
    print("----------------------------------------------------------------")

print("end loop")
print("waiting time :{}".format(waiting_time))
if wait_history == []:
    print("No waiting")
else:
    print(wait_history)