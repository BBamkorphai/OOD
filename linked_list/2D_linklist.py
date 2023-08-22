class node:
    def __init__(self, data, next=None, s_next=None):
        self.data = data
        self.next = next
        self.s_next = s_next

    def __str__(self):
        return str(self.data)
    
class Snode:
    def __init__(self, data, s_next=None):
        self.data = data
        self.s_next = s_next

    def __str__(self):
        return str(self.data)
class link:
    def __init__(self):
        self.head = None

    def next_node(self,data):
        new_node = data
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def search(self,data):
        count = 0
        current_node = self.head
        while current_node is not None:
            if str(current_node) == str(data):
                return count
            count += 1
            current_node = current_node.next
        count = -1
        #print("Not found")
        return count


    def next_secondary_node(self,n,data): # data = class_Snode
        count = 0
        current = self.head
        while count != self.search(n):
            count += 1
            current = current.next
        #print(current)    
        while current.s_next is not None:
            current = current.s_next
        current.s_next = data
        

    def show_all(self):
        current_node_main = self.head
        main_history = []

        while current_node_main is not None:
            #print(f'main history : {main_history}')
            if current_node_main.data not in main_history:
                #print("pass1")
                main_history.append(current_node_main.data)
                final_str = f'{current_node_main} : '
                current_node_sub = current_node_main
                first = 0
                while current_node_sub is not None:
                    if first != 0:
                        final_str += str(current_node_sub.data)
                        final_str += ","
                    first = 1
                    current_node_sub = current_node_sub.s_next
                current_node_main = current_node_main.next
                print(final_str)
            else:
                #print("pass2")
                current_node_main = current_node_main.next

inp = input("input : ").split(",")
l = link()
for i in inp:
    u = i.split(" ")
    if u[0] == "ADN":
        #print(u[1])
        l.next_node(node(u[1]))
    elif u[0] == "ADSN":
        h = u[1].split("-")
        #print(h[0], h[1])
        l.next_secondary_node(h[0],Snode(h[1]))
#print(l.search("C"))
l.show_all()