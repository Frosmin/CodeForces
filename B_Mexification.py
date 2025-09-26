from collections import deque

n = int(input())
for _ in range(n):
    n,k = map(int,input().split())
    lst = list(map(int, input().split()[:n]))
    lst.sort()
    if lst[0] != 0 :
       numerito = lst[0]
       print(numerito)
    else:
        print(lst[-1] + 1)
         