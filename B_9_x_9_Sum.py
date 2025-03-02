n = int (input())
res = 0
for i in range(10):
    for j in range(10):
        m = i*j
        if m != n:
            res += m
print (res)