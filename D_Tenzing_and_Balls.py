
for _ in range(int(input())):
    n=int(input())+1
    a=[0]*n
    b=[n]*n
    for i, j in enumerate(map(int, input().split())):
        a[i+1]=min(a[i] + 1, b[j])
        b[j]=min(a[i], b[j])
    print(n-a[-1]-1)