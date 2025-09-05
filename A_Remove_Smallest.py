def res(a,b):
    if abs(a-b) <=1 :
        return True
    else:
        return False
    



t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    lst.sort()
    # print(lst)
    bb = True
    if n == 1:
        print("YES")
        continue
    for i in range(n-1):
        
        if res(lst[i], lst[i+1]):
            pass
        else:
            print("NO")
            bb = False
            break
    if bb :
        print("YES")
            
        