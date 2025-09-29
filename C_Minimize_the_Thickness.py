# n = int(input())
# for _ in range(n):
#     k = int(input())
#     lst = list(map(int, input().split()[:k]))







 
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()[:n]))
 
    s, total = 0, n
    
    for i in range(n):
        s += arr[i]
        q = 0
        pos = False
        mejor, ultimo = 0, i
        for j in range(i+1, n):
            q += arr[j]
            if q == s:
                q = 0
                mejor = max(mejor, j-ultimo)
                ultimo = j
                if j == n-1:
                    pos = True
            elif q > s:
                mejor = 0
                break
        if pos:
            total = min(total, max(mejor, i+1))
    print(total)