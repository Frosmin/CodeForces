

n,m,a,b = map(int, input().split())

if n < m:
    print(b)
    exit()

if n%2 == 0: #par
    res1 = n*a
    if m%2 == 0: #par
        res2 = (n//m) * b
    else:
        if n/m == n//m:
            res2 = (n//m) * b
        else:
            res2 = ((n//m) * b) + m
else:
    res1 = n*a
    if m%2 == 0:
        res2 = (n//m)#2
        total = n - res2*m
        res2 = (total * a) + (res2 * b)
    else:
        if n/m == n//m:
            res2 = (n//m) * b
        else:
            res2 = ((n//m) * b) + m
            
print(min(res1, res2))
###
#n m a b 
# 5 2 2 3 


#m cantidad de viajes que cubre el pasaje 

n, m, a, b = map(int, input().split())

cost1 = n * a
cost2 = (n // m) * b + (n % m) * a
cost3 = ((n + m - 1) // m) * b

print(min(cost1, cost2, cost3))