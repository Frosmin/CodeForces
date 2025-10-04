from math import sqrt

def ceildiv(a,b):
    return -(a//-b)


def cost(a,b,m):
    return ceildiv(a,m) + ceildiv(b,m) + m - 1 
 


for _ in range(int(input())):

    a,b = map(int,input().split())
    c = int(sqrt(a+b))

    lower = max(1, c - 10**4)
    upper = c + 10**4

    ans = float('inf')
    for i in range(lower, upper+1):
        ans = min(ans, cost(a,b,i))
    print(ans)
 
    
