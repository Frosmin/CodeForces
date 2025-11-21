from collections import defaultdict

 
dict = defaultdict(set)
m = 0
for _ in range(int(input())):
    s = input()
    m = len(s)
    for i in range(len(s)):
        if s[i] != '?':
            dict[i].add(s[i])


res = []
for i in range(m):
    if i in dict:
        l = list(dict[i])
        if len(l) == 1:
            res.append(l[0])
        else:
            res.append('?') 
    else:
        res.append('a')
print(*res,sep='')