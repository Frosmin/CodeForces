s = input().strip()
n = len(s)
 
pires = [0] * n
j = 0
for i in range(1, n):
    while j and s[i] != s[j]:
        j = pires[j-1]
    if s[i] == s[j]:
        j += 1
    pires[i] = j
 
x = pires[-1]
 

if x > 0 and x in pires[:-1]:
    print(s[:x])
else:
    x = pires[x-1]
    if x > 0:
        print(s[:x])
    else:
        print("Just a legend")