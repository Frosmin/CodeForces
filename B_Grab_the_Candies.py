for ii in range(int(input())):
    n = int(input())
    bags = list(map(int, input().split()))
    
    impar = 0
    par = 0
 
    for b in bags:
        if b % 2 == 0:
            par +=b
        else:
            impar +=b
 
    if par > impar:
        print("YES")
    else:
        print("NO")