from collections import deque


n = int(input())
lst = list(map(int, input().split()[:n]))
cola = deque([lst[0]])
res = 0

if n == 1:
    print(0)
    exit()

for item in lst:
    if cola[0] > item:
        cola.appendleft(item)
        res+=1
    if cola[-1] < item:
        cola.append(item)
        res+=1
print(res)