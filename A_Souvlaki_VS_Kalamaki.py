t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    a.sort()
    valid = True
    for i in range(1, n-1, 2):
        if a[i] != a[i+1]:
            valid = False
            break
    print("YES" if valid else "NO")