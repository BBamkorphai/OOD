class Bus:
    def __init__(self, people, fare) -> None:
        self._people = people
        self._fare = fare

    @property
    def people(self):
        return self._people
    
    @property
    def fare(self):
        return self._fare
    
    def __str__(self):
        return 'this bus has ' + str(self._people) \
        + ' people with fare = ' + str(self._fare)
    
    def __lt__(self,rhs):
        return self._people * self._fare < rhs._people * rhs._fare
    
    def people_in(self, k):
        self._people += k

    def people_out(self, k):
        self._people -= k
        if int(self._people) < 0:
            self._people = 0

    def change_fare(self, new_fare):
        self._fare = new_fare
        

b1, b2, f1, f2 = input("Enter people in Bus1, Bus2, fare Bus1, Bus2 : ").split()
b1 = Bus(int(b1), int(f1))
b2 = Bus(int(b2), int(f2))
if b1 < b2:
    print(b1)
else:
    print(b2)
b1.people_in(3)
b1.people_out(6)
b1.change_fare(12)
print(b1)