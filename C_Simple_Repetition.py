
def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True


    
t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    if es_primo(int(str(n) * k)):
        print("YES")
    else:
        print("NO")
        
        
        
# import math

# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     max_divisor = int(math.sqrt(n)) + 1
#     for d in range(3, max_divisor, 2):
#         if n % d == 0:
#             return False
#     return True

# t = int(input())
# for _ in range(t):
#     x, k = map(int, input().split())
#     if k == 1:
#         print("YES" if is_prime(x) else "NO")
#     else:
#         if x == 1 and k == 2:
#             print("YES")
#         else:
#             print("NO")