# import sys
# from array import array


# def solve() -> None:
#     data = list(map(int, sys.stdin.buffer.read().split()))
#     if not data:
#         return
#     it = iter(data)
#     n = next(it)
#     m = next(it)
#     stride = n + 1
#     size = stride * stride
#     best = [array('I', [0]) * size for _ in range(n + 1)]

#     for _ in range(m):
#         w = next(it)
#         l = next(it)
#         r = next(it)
#         idx = l * stride + r
#         for pivot in range(l, r + 1):
#             arr = best[pivot]
#             if w > arr[idx]:
#                 arr[idx] = w

#     for pivot in range(1, n + 1):
#         arr = best[pivot]
#         for length in range(1, n + 1):
#             min_l = max(1, pivot - length + 1)
#             max_l = min(pivot, n - length + 1)
#             if min_l > max_l:
#                 continue
#             for l in range(min_l, max_l + 1):
#                 r = l + length - 1
#                 idx = l * stride + r
#                 val = arr[idx]
#                 if l < pivot:
#                     nxt = arr[(l + 1) * stride + r]
#                     if nxt > val:
#                         val = nxt
#                 if r > pivot:
#                     nxt = arr[l * stride + (r - 1)]
#                     if nxt > val:
#                         val = nxt
#                 arr[idx] = val

#     dp = [[0] * (n + 2) for _ in range(n + 2)]
#     for length in range(1, n + 1):
#         for l in range(1, n - length + 2):
#             r = l + length - 1
#             best_split = 0
#             for k in range(l, r):
#                 val = dp[l][k] + dp[k + 1][r]
#                 if val > best_split:
#                     best_split = val
#             res = best_split
#             idx = l * stride + r
#             for pivot in range(l, r + 1):
#                 w = best[pivot][idx]
#                 if w == 0:
#                     continue
#                 total = w
#                 if pivot > l:
#                     total += dp[l][pivot - 1]
#                 if pivot < r:
#                     total += dp[pivot + 1][r]
#                 if total > res:
#                     res = total
#             dp[l][r] = res

#     print(dp[1][n])


# if __name__ == "__main__":
#     solve()



import sys
from array import array


def solve():
    with open('pieaters.in', 'rb') as fh:
        data = list(map(int, fh.read().split()))
    if not data:
        with open('pieaters.out', 'w') as out:
            out.write('0\n')
        return

    it = iter(data)
    n = next(it)
    m = next(it)
    stride = n + 1
    size = stride * stride
    best = [array('I', [0]) * size for _ in range(n + 1)]

    for _ in range(m):
        w = next(it)
        l = next(it)
        r = next(it)
        idx = l * stride + r
        for pivot in range(l, r + 1):
            arr = best[pivot]
            if w > arr[idx]:
                arr[idx] = w

    for pivot in range(1, n + 1):
        arr = best[pivot]
        for length in range(1, n + 1):
            min_l = max(1, pivot - length + 1)
            max_l = min(pivot, n - length + 1)
            if min_l > max_l:
                continue
            for l in range(min_l, max_l + 1):
                r = l + length - 1
                idx = l * stride + r
                val = arr[idx]
                if l < pivot:
                    nxt = arr[(l + 1) * stride + r]
                    if nxt > val:
                        val = nxt
                if r > pivot:
                    nxt = arr[l * stride + (r - 1)]
                    if nxt > val:
                        val = nxt
                arr[idx] = val

    dp = [[0] * (n + 2) for _ in range(n + 2)]
    for length in range(1, n + 1):
        for l in range(1, n - length + 2):
            r = l + length - 1
            best_split = 0
            for k in range(l, r):
                val = dp[l][k] + dp[k + 1][r]
                if val > best_split:
                    best_split = val
            res = best_split
            idx = l * stride + r
            for pivot in range(l, r + 1):
                w = best[pivot][idx]
                if w == 0:
                    continue
                total = w
                if pivot > l:
                    total += dp[l][pivot - 1]
                if pivot < r:
                    total += dp[pivot + 1][r]
                if total > res:
                    res = total
            dp[l][r] = res

    with open('pieaters.out', 'w') as out:
        out.write(str(dp[1][n]) + '\n')


if __name__ == "__main__":
    solve()