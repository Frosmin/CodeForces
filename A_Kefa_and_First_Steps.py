n = int(input())
lst = list(map(int,input().split()[:n]))
maxi = 0
res = 0
ant = 0
for i in range(n):
    if lst[i] >= ant:
        ant = lst[i]
        res+=1
    else:
        if maxi < res:
            ant  = lst[i]
            maxi = res
            res = 1
if maxi < res:
            maxi = res
            res = 0 
print(maxi)
    
    