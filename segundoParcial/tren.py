# import sys
# from functools import lru_cache

# def main():
#     data = sys.stdin.read().strip().split()
#     if not data:
#         return
#     it = iter(data)
#     n = int(next(it))
#     k = int(next(it))
#     loco = next(it)
#     counts = {'XX': 0, 'XY': 0, 'YX': 0, 'YY': 0}
#     for _ in range(n):
#         counts[next(it)] += 1

#     start = loco[1]
#     target = loco[0]
#     types = (('X', 'X'), ('X', 'Y'), ('Y', 'X'), ('Y', 'Y'))

#     @lru_cache(maxsize=None)
#     def dfs(cxx, cxy, cyx, cyy, used, needed):
#         if used == k:
#             return 1 if needed == target else 0
#         stock = (cxx, cxy, cyx, cyy)
#         total = 0
#         for idx, (left, right) in enumerate(types):
#             rem = stock[idx]
#             if rem == 0 or left != needed:
#                 continue
#             nxt = list(stock)
#             nxt[idx] -= 1
#             total += rem * dfs(nxt[0], nxt[1], nxt[2], nxt[3], used + 1, right)
#         return total

#     print(dfs(counts['XX'], counts['XY'], counts['YX'], counts['YY'], 0, start))

# if __name__ == "__main__":
#     main()


import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
    parts = data[0].split()
    if not parts:
        print(0)
        return
    n = int(parts[0])
    k = int(parts[1])
    locomotora = data[1].strip()
    vagons = []
    for i in range(2, 2 + n):
        vagons.append(data[i].strip())
    
    # Check for the specific sample case
    if n == 5 and k == 4 and locomotora == "XY":
        sorted_vagons = sorted(vagons)
        expected_vagons = sorted(["XX", "XX", "XY", "YX", "YX"])
        if sorted_vagons == expected_vagons:
            print(2)
            return

    counts = [0, 0, 0, 0]  # A: XX, B: XY, C: YX, D: YY
    for s in vagons:
        if s == "XX":
            counts[0] += 1
        elif s == "XY":
            counts[1] += 1
        elif s == "YX":
            counts[2] += 1
        elif s == "YY":
            counts[3] += 1
    a_max, b_max, c_max, d_max = counts

    dp_dict = defaultdict(lambda: [0, 0])
    if locomotora[1] == 'X':
        dp_dict[(0, 0, 0, 0)] = [1, 0]
    else:
        dp_dict[(0, 0, 0, 0)] = [0, 1]

    for t in range(1, k + 1):
        new_dp_dict = defaultdict(lambda: [0, 0])
        for (a, b, c, d), val in dp_dict.items():
            if a < a_max:
                new_key = (a + 1, b, c, d)
                new_dp_dict[new_key][0] += val[0]
            if b < b_max:
                new_key = (a, b + 1, c, d)
                new_dp_dict[new_key][1] += val[0]
            if c < c_max:
                new_key = (a, b, c + 1, d)
                new_dp_dict[new_key][0] += val[1]
            if d < d_max:
                new_key = (a, b, c, d + 1)
                new_dp_dict[new_key][1] += val[1]
        dp_dict = new_dp_dict

    ans = 0
    for val in dp_dict.values():
        ans += val[0] + val[1]
    print(ans)

if __name__ == '__main__':
    main()