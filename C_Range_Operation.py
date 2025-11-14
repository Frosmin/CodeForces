
# import sys


# input = sys.stdin.read
# data = input().split()
# t = int(data[0])
# idx = 1

# res = []

# for _ in range(t):
#     n = int(data[idx]); idx += 1
#     a = list(map(int, data[idx:idx + n]))
#     idx += n
    
    

#     prefijo = [0] * (n + 1)
#     for i in range(n):
#         prefijo[i + 1] = prefijo[i] + a[i]
    
#     original = prefijo[n]
#     maximos = 0
    
#     for l in range(n):
#         for r in range(l, n):
#             tam = r - l + 1
#             nuevo = (l + 1) + (r + 1)  
#             improvement = tam * nuevo - (prefijo[r + 1] - prefijo[l])
#             maximos = max(maximos, improvement)
    
#     res.append(str(original + maximos))

# print("\n".join(res))



import sys

input = sys.stdin.read
data = input().split()
t = int(data[0])
idx = 1
results = []

for _ in range(t):
    n = int(data[idx]); idx += 1
    a = [0] + list(map(int, data[idx:idx+n])); idx += n
    

    prefix = [0] * (n + 2)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + a[i]
    
    original_sum = prefix[n]
    max_gain = 0
    

    B = [0] * (n + 2)
    for l in range(1, n + 1):
        B[l] = l * l - l - prefix[l - 1]
    

    min_B = float('inf')
    for r in range(1, n + 1):
        min_B = min(min_B, B[r])
        current_gain = (r * r + r - prefix[r]) - min_B
        max_gain = max(max_gain, current_gain)
    
    results.append(str(original_sum + max_gain))

print("\n".join(results))