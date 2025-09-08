t = int(input())


for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()[:n]))

    group0 = [i for i in range(1, n+1) if i % 3 == 0] 
    group1 = [i for i in range(1, n+1) if i % 3 == 1]  
    group2 = [i for i in range(1, n+1) if i % 3 == 2]  

    q = [0] * n
        
    for i in range(n):
            if p[i] % 3 == 0 and group0:
                q[i] = group0.pop()
            elif p[i] % 3 == 1 and group2:
                q[i] = group2.pop()
            elif p[i] % 3 == 2 and group1:
                q[i] = group1.pop()
            else:
                if group0:
                    q[i] = group0.pop()
                elif group1:
                    q[i] = group1.pop()
                else:
                    q[i] = group2.pop()
    print(*q)