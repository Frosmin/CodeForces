n = int(input())
lst = list(map(int, input().split()[:n]))

maximon = max(lst)
res = 0

for item in lst:
    res += maximon-item
print(res)