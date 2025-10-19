for _ in range(int(input())):
    w = input()
    n = len(w)
    a = "" 
    a += w[0]
    for i in range(1, n-1, 2):
        a += w[i]
    a += w[n-1]

    print(a)