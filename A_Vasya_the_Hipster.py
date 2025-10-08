a,b = map(int, input().split())

minimo = min(a,b)
res = minimo
print(res, end=" ")
print((max(a,b) - minimo) // 2)
