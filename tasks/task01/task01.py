for b in range(1, 1001):
    # define the number of digits
    power = 0
    a = b
    c = b
    while b:
        power += 1
        b = b // 10
    s = 0
    while a:
        s += pow(a % 10, power)
        a = a // 10
    if c == s:
        print(c)
