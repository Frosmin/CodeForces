for _ in range(int(input())):
    n =int(input())
    pal = input()

    res = pal.count(pal[-1])
    print(n-res)

    
    