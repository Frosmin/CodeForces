n = int(input())
for _ in range(n):
    a,b,c = list(map(int,input().split()))
    maximo = max(a,b,c)
    if maximo == a:
        print("YES" if b+c == a else "NO")
    elif maximo == b:
        print("YES" if a+c == b else "NO")
    elif maximo == c:
        print("YES" if a+b == c else "NO")