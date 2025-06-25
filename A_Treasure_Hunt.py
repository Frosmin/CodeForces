t = int(input())
for _ in range(t):
    x, y, a = map(int, input().split())
    two_a_plus_1 = 2 * a + 1
    if 2 * x > two_a_plus_1:
        print("NO")
        continue
    s = x + y
    if 2 * s > two_a_plus_1:
        print("YES")
        continue
    denominator = 2 * s
    k_full = two_a_plus_1 // denominator
    sum_2k = k_full * s
    sum_after_B = sum_2k + x
    if 2 * sum_after_B > two_a_plus_1:
        print("NO")
    else:
        print("YES")