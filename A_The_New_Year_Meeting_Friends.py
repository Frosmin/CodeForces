lst = list(map(int,input().split()[:3]))
lst.sort()
res = 0
res += lst[1]-lst[0]
res +=  lst[2]-lst[1]
print(res)

