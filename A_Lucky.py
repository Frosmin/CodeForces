n = int(input())
for _ in range(n):
    lst = list(map(int, input()))
    lst1 = lst[0:3]
    lst2 = lst[3:6]
    print("YES" if sum(lst1) == sum(lst2) else "NO")