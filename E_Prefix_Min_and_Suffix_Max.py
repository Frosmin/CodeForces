# def llegar(n, lst):
#     res = ""
#     mamixo = max(lst)
#     minimo= min(lst)
#     for i  in range(n):
#         if i == 0 or n-1 == i:
#             res += "1"
#         elif lst[i] == mamixo or lst[i] == minimo:
#             res += "1"
#         else:
#             res += "0"
#     return res
         




# n = int(input())
# for _ in range(n):
#     k = int(input())
#     lst = list(map(int, input().split()[:k]))
#     print(llegar(k,lst))



t = int(input())
 
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()[:n]))
    l = 0
    r= n-1
 
    mn,mx = arr[l], arr[r]
 
    res = [0] * n
    res[l] = 1
    res[r] = 1
    l += 1
    r -= 1
 
 
    while l < n:
        if arr[l] < mn:
            res[l] = 1
            mn = arr[l]
        if arr[r] > mx:
            res[r] = 1
            mx = arr[r]
 
        l += 1
        r -= 1

    
    print(''.join(str(x) for x in res))