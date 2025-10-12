n,k = map(int,input().split())
lst = list(map(int,input().split()[:n]))
lst.sort()
# print(lst)
res = 0
for item in lst:
    if 5-item >= k:
        res+=1

print(res//3)
