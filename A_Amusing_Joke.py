jefe = input()
secuas = input()
new = jefe+secuas

mescla = input()
dic1 = {}
dic2 = {}
for item in new:
    if item in dic1:
        dic1[item] += 1
    else:
        dic1[item] = 1
        
for item in mescla:
    if item in dic2:
        dic2[item] += 1
    else:
        dic2[item] = 1
        

print("YES" if dic1 == dic2 else "NO")