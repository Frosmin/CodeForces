n = int(input())
lst = list(map(int, input().split()[:n]))
max_len = 1
actual_len = 1
for i in range(n - 1):
    if lst[i] <= lst[i+1]:
        actual_len += 1
    else:
        max_len = max(max_len, actual_len)
        actual_len = 1
        
print(max(max_len, actual_len)) 
    
    