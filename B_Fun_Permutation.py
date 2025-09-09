def euclides(a,b):
    if b == 0:
        return a
    else:
        return euclides(b, a%b)
    

t = int(input())
for _ in range(t):
    new = []
    n = int(input())
    lst = list(map(int, input().split()[:n]))
    for i in range(n):
        new.append(n-lst[i]+1)
    print(" ".join(map(str,new)))
    

    