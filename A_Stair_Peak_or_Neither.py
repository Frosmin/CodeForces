for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if a < b and b < c:
        print("STAIR")
    elif b > a and b > c:
        print("PEAK")
    else:
        print("NONE")
