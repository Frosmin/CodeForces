n = int(input())
sarr = []
 
for i in range(n):
    sarr.append((input(), 0))
 
t = input()
 
 
index = 0
 
res = []
 
for c in t:
    activos = []
    for s, i in sarr:
        while i < len(s) and s[i] != c:
            res.append(s[i])
            i += 1
        if i < len(s):
            activos.append((s, i+1))
    
    if len(activos) == 0:
        break
    sarr = activos
    res.append(t[index])
    index += 1
    if index == len(t):
        break
 
 
if index == len(t):
    print("NO")
else:
    print("YES")
    print(''.join(res))