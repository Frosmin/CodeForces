# t = int(input())
# for _ in range(t):
#     n = len(str(input()))
#     if n % 2 == 0:
#         print(n//2)
#     else:
#         print(n-1) 


t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    prefix_zeros = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_zeros[i] = prefix_zeros[i-1] + (1 if s[i-1] == '0' else 0)
    max_length = 1
    for j in range(n):
        if s[j] != '0':
            zeros_before = prefix_zeros[j]
            current_length = zeros_before + 1
            if current_length > max_length:
                max_length = current_length
    print(n - max_length)