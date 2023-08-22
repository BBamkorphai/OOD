def partitions(n, s, m=None, holding_list=[]):
    global lines_printed
    if m is None:
        m = n
    if n == 0:
        if holding_list == "":
            print(n)
        elif lines_printed < s:
            print(" + ".join(holding_list))
            lines_printed += 1
        elif lines_printed == s:
            print('. . .')
            lines_printed += 1
        return 1
    if n < 0 or m == 0:
        return 0
    with_m = partitions(n - m, s, m, holding_list + [str(m)])
    without_m = partitions(n, s, m - 1, holding_list)
    return with_m + without_m


lines_printed = 0
n, s = map(int ,input('Enter n, s: ').split())
count = partitions(n, s)
print(f"Total: {count}")