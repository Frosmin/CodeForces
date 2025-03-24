t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
        continue
    permutation = [2, 1]
    if n > 2:
        permutation += list(range(3, n + 1))
    print(' '.join(map(str, permutation)))