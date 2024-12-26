k, n, w = map(int, input().split())
r = 0

if not (1 <= k, w <=1000, 0<= n <= 10**9):
    raise ValueError("Error")

for i in range(1, w+1):
    r = r+(i*k)
res = r - n

print (max(0,res))