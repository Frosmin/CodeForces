n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    res = 0
    if abs(b-a)%10 != 0:
        res += 1
    res += abs(b-a)//10
    print(res)