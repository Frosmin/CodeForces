for _ in range(int(input())):
    lst = list(map(int,input().split()[:2]))
    print(*sorted(lst))