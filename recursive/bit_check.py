n = int(input("Enter Number : "))

def target_input(a):
    if a>=0 :
        return bin((pow(2,a)) - 1)[2:]

def run_bit(n, count, target): #count vthe round target is target binary
        if n < 0:
            print("Only Positive & Zero Number ! ! !")
        else:
            a = bin(count)[2:]
            while len(a) < len(target):
                 a = str(0) + str(a)

            if str(a) != str(target):
                count += 1
                print(a)
                run_bit(n, count, target)
            else:
                print(a)

run_bit(n, 0, target_input(n))