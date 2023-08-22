def staircase(n, round = 0, str_out = ''):
    if n > 0:
        if round < n:
            if len(str_out) != n:
                if n - round <= len(str_out) + 1:
                    str_out += str("#")
                else:
                    str_out += str('_')
                staircase(n, round, str_out)
            else:
                round += 1
                print(str_out)
                str_out = ""
                staircase(n, round, str_out)
        else:
            pass
    elif n == 0:
        print("Not Draw!")
    else:
        #print("pass 555")
        if round < abs(n):
            if len(str_out) != abs(n):
                if round - len(str_out) - 1 < 0:
                    str_out += str("#")
                else:
                    str_out += str('_')
                staircase(n, round, str_out)
            else:
                round += 1
                print(str_out)
                str_out = ""
                staircase(n, round, str_out)
        else:
            pass
        
    

staircase(int(input("Enter Input : ")))