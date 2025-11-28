t=int(input())
for _ in range(t):
    n, maximo = map(int, input().split())
    s = input()
    t = input()
 
    if s[0] != t[0]:
        print(-1)
        continue
    
    if s == t:
        print(0)
        continue
    
    pos = n-1
    stps = []
    for i in range(n-1, -1, -1):
        for j in range(min(pos, i), -1, -1):
            if t[i] == s[j]:
                stps.append(i-j)
                pos = j
                break
 
    if len(stps) < n:
        print(-1)
        continue
    
    stps.reverse()
    mx = max(stps)
    if mx > maximo:
        print(-1)
        continue
 
    print(mx)
    for i in range(1, mx+1):
        sdash = [s[0]]
        for j in range(1, n):
            if stps[j] >= i:
                sdash.append(s[j-1])
            else:
                sdash.append(s[j])
        
        s = "".join(sdash)
        print(s)