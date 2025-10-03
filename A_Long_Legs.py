import math


for _ in range(int(input())):
    a, b = map(int, input().split())
    S = a + b
    if S == 0:
        print(0)
    else:
        best = float('inf')
        k_max = 2 * int(math.isqrt(S)) + 10
        for k in range(0, k_max + 1):
            s = (S + k) // (k + 1)
            total_moves = k + s
            if total_moves < best:
                best = total_moves
        print(best)
  
