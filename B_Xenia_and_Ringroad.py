n,m = map(int,input().split())
lst = list(map(int,input().split()[:m]))
actual = 1
res = 0



for i in range(m):
    if i == 0:
        res += (lst[0])-1
        actual = lst[0]
    else:
        if actual <= lst[i]:
            res += lst[i] -actual
            actual = lst[i]
        else:
            res+= ((n-actual)+ lst[i])
            actual = lst[i]
print(res)