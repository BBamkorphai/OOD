def format_print(holding_list, count=0, out_str=''):
    if count <= len(holding_list) - 1:
        out_str += str(holding_list[count])
        count += 1
        if count < len(holding_list):
            out_str += ' + '
        format_print(holding_list, count, out_str)
    else:
        print(out_str)

def printCombinationsRec(i, n, out, index):
    if n == 0:
        a = out[:index]
        format_print(a)
        return

    if i > n:
        return

    # First, consider the larger values
    for j in range(n, 0, -1):
        out[index] = j
        printCombinationsRec(j, n - j, out, index + 1)

def printCombinations(n):
    out = [None] * n
    printCombinationsRec(1, n, out, 0)

if __name__ == '__main__':
    n = 5
    printCombinations(n)