    

for _ in range(int(input())):
    n, k, x = map(int, input().split())
    sum = 0
    nk = n-k
    total = (n*(n+1))/2
    fke = (nk*(nk+1))/2
    second = total-fke
    first = (k*(k+1))/2
    if first <= x <= second:
            print("YES")
    else:
            print("NO")