n = int(input())
for _ in range(n):
    t,x = map(int,input().split())
    for i in range(t):
        x *= 2

    print(x)