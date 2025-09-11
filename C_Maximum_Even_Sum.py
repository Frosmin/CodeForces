# import math

# def divi(b):
#     lst = set()
#     for i in range(1, int(math.sqrt(b)) + 1):
#         if b % i == 0:
#             lst.add(i)
#             lst.add(b // i)
#     return list(lst)


# n = int(input())
# for _ in range(n):
#     a,b = map(int,input().split())
#     divisores = divi(b)
#     res = 0
#     for k in divisores:
#         suma = (a*k) + (b//k)
#         if suma > res and suma % 2 == 0:
#             res = suma
#     print(-1 if res== 0 else res)



def solve():
    a,b = map(int, input().split()) 


t = int(input())
for _ in range(t):
    solve()