# from collections import deque

# t = int(input())
# lst = list(map(int,input().split()[:t]))
# n = int(input())
# cola = deque()
# res = []

# for i , item in enumerate(lst):

    
#     while cola and lst[cola[-1]] <= item:
#         cola.pop()
#     cola.append(i)

#     if cola[0] <= i-n:
#         cola.popleft()

#     if i >= n-1:
#         res.append(lst[cola[0]])
# print(*res)




from collections import deque

n = int(input())
lst = list(map(int,input().split()[:n]))
k = int(input())
cola = deque()


for i in range(n):
    if cola and cola[0] <= i - k:
        cola.popleft()
    
    while cola and lst[cola[-1]] <= lst[i]:
        cola.pop()
    cola.append(i)

    if i >= k -1:
        print(lst[cola[0]], end=" ")





