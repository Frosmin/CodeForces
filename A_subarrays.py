import collections


n = int(input())
arr = list(map(int, input().split()[:n]))
k = int(input())

dq = collections.deque()
result = []

for i in range(n):
    if dq and dq[0] == i - k:
        dq.popleft()
        
    while dq and arr[dq[-1]] < arr[i]:
        dq.pop()
        
    dq.append(i)
    
    if i >= k - 1:
        result.append(str(arr[dq[0]]))
        
print(" ".join(result))