for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    cruces = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] >= a[j]:
                cruces += 1
    
    print(cruces)