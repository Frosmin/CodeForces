# import sys

# input = sys.stdin.read
# data = input().split()

# iterator = iter(data)
# t = int(next(iterator))

# results = []

# for _ in range(t):
#     n = int(next(iterator))
#     px = int(next(iterator))
#     py = int(next(iterator))
#     qx = int(next(iterator))
#     qy = int(next(iterator))
    
#     a = []
#     for _ in range(n):
#         a.append(int(next(iterator)))
        
#     sum_a = sum(a)
#     max_a = max(a)
    
    
#     dist_sq = (px - qx)**2 + (py - qy)**2
    
    
#     if dist_sq > sum_a**2:
#         results.append("No")
#         continue
        
    
#     rhs = 2 * max_a - sum_a
#     if rhs > 0:
#         if dist_sq < rhs**2:
#             results.append("No")
#             continue
            
#     results.append("Yes")





