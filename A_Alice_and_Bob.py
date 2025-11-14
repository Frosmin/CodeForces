t = int(input().strip())
for _ in range(t):
    data = input().split()
    n = int(data[0])
    a = int(data[1])
    v = list(map(int, input().split()))
    L = 0
    R = 0
    for num in v:
        if num < a:
            L += 1
        elif num > a:
            R += 1
    if R > L:
        print(a + 1)
    elif L > R:
        print(a - 1)
    else:
        print(1337)