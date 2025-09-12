w, h  = map(int, input().split())
t = int(input())
res = 0
for _ in range(t):
    lst = list(map(int,input().split()))
    if w in lst and h in lst:
        res+=1
if res > 1:
    print("N")
else:
    print("Y")