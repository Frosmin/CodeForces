for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if (a+b+c) - min(a,b,c) >= 10:
        print("YES")
    else:
        print("NO") 