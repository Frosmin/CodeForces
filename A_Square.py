for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    print("YES" if a == b and a == c and a == d else "NO")