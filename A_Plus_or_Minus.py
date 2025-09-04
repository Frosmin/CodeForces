n = int(input())
for _ in range(n):
    a,b,r = map(int,input().split())
    print("+" if a+b ==r else "-")

    