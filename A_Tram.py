n = int(input())
estan  = 0
max = 0 
for _ in range(n):
    salen,entran = map(int, input().split())
    estan -= salen 
    estan += entran
    if estan > max :
        max = estan
print(max)

