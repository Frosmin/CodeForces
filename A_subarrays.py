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
mayor = 0

for i in range(n):

    if i >= k:
            print(max(cola), end=" ")


    if len(cola) == k:
          cola.popleft()
    cola.append(lst[i])


print(max(cola))







n = int(input())
lst = list(map(int,input().split()[:n]))
k = int(input())
mayor = 0

for i in range(0, n - k + 1):
        mayor = 0
        for j in range(i, i + k):
            if lst[j] > mayor:
                mayor = lst[j]
        print(mayor, end=" ")


# for i in range(n):
#     if cola and cola[0] <= i - k:
#         cola.popleft()
    
#     while cola and lst[cola[-1]] <= lst[i]:
#         cola.pop()
#     cola.append(i)

#     if i >= k -1:
#         print(lst[cola[0]], end=" ")





