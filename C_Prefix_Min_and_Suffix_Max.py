# import sys
# input = lambda: sys.stdin.readline().rstrip()
 
 
for _ in range(int(input())):


    n = int(input())
    lst = list(map(int, input().split()))



    elst = [0]*n #llena lista con ceros :D
    elst[0] = 1
    c = lst[0]
    
    for i in range(1,n):
        if lst[i] < c:
            elst[i] = 1
        c = min(c, lst[i])

    c = 0
    for i in range(n-1, -1, -1):
        if lst[i] > c:
            elst[i] = 1
        c = max(c, lst[i])
    print(''.join(map(str, elst)))