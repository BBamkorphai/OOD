class Queue:
    def __init__(self, list = None):
        if list == None:
            self.queue = []
        else:
            self.queue = list

    def __str__(self):
        p = 'Queue: '
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
        
    def is_in(self, item):
        if item in self.queue:
            return True
        else:
            return False
        
    def my_queue(self):
        return self.queue

def extract_integers_from_string(input_string):
    return [s for s in input_string.split() if s.isdigit()]


input_str = input("Enter width, height, and room: ").split(" ")
poping = []
#print(poping)
input_list = []

for i in range(len(input_str)):
    if i == 0 or i == 1:
        poping.append(input_str[i])
    else:
        input_list.append(input_str[i])

# print(poping)
# print(input_list)
input_list = list(input_list[0])
# print(input_list)

map = []
bus = []

give_size = 0
#print(input_list)

for i in input_list:
    if i != ' ':
        if i != ',':
            give_size += 1
            bus.append(i)
        else:
            map.append(bus)
            bus = []
map.append(bus)

#print(give_size)
a_x = int(poping[0])
a_y = int(poping[1])
aspect_size = a_x * a_y
#print(aspect_size)
# print(input_list)
#print(map)
#print(map[2][5])

done = 0
# start = 1

def find_start(input_list: list):
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            if input_list[i][j] == 'F':
                return [j, i]
            
def find_end(input_list: list):
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            if input_list[i][j] == 'O':
                return True
    return False
            
def next_move(map:list, position_now:str):
    x = int(position_now[0])
    y = int(position_now[1])
    bus = []
    # north check
    #print(map[y][x])
    if y - 1 >= 0:
        if map[y - 1][x] == '_' or map[y - 1][x] == 'O':
            
            bus.append([x,y - 1])

    # east check
    if x + 1 <= a_x - 1:
        if map[y][x + 1] == '_' or map[y][x + 1] == 'O':
            bus.append([x + 1,y])

    #south check
    if y + 1 <= a_y - 1:
        if map[y + 1][x] == '_' or map[y + 1][x] == 'O':
            bus.append([x,y + 1])

    #west check
    if x - 1 >= 0:
        if map[y][x - 1] == '_' or map[y][x - 1] == 'O':
            bus.append([x - 1, y])

    return bus

def check_out(map:list, next_pos):
    #print(f"next pos:{next_pos}")
    #print(map[next_pos[1]][next_pos[0]])
    if map[next_pos[1]][next_pos[0]] == 'O':
        return True
    else:
        return False
    
def format_coordinates(coordinates):
    queue = []
    for coord in coordinates:
        queue.append(tuple(coord))
    return "Queue: " + str(queue)
    
#print("F" not in input_list)
#print(aspect_size != give_size)
#print(input_list)

if "F" not in input_list or aspect_size != give_size:
    print("Invalid map input.")
else:
    q1 = Queue()
    history_queue = Queue()
    my_pos = find_start(map)
    #print(f"mypos :{my_pos}")
    q1.enqueue(my_pos)
    history_queue.enqueue(my_pos)
    #print(f"q1 is :{q1}")
    if find_end(map):
        while done == 0:
            if not q1.is_empty():  
                print(format_coordinates(q1.my_queue()))
                pos = q1.dequeue()
                will_move = next_move(map ,pos) # list
                #print(f"will move :{will_move}")
                for i in will_move:
                    if not q1.is_in(i) and not history_queue.is_in(i):
                        q1.enqueue(i)
                        history_queue.enqueue(i)
                    if check_out(map ,i):
                        print("Found the exit portal.")
                        done = 1
            else:
                print("Cannot reach the exit portal.")
                done = 1
            
    else:
        print(format_coordinates(q1.my_queue()))
        #print("pass")
        print("Cannot reach the exit portal.")
        #print("--------------------------------")
        
