# import sys

# n = int(input())
# if n % 4 == 0 or n % 7 == 0:
#     print("YES")
#     exit()

# n = str(n)
# res = any(caracter != "7" and caracter != "4" for caracter in n)
# print("YES" if not res else "NO")



# import sys

# n = int(sys.stdin.readline())
# lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

# is_almost_lucky = False
# for lucky_num in lucky_numbers:
#     if n % lucky_num == 0:
#         is_almost_lucky = True
#         break

# if is_almost_lucky:
#     sys.stdout.write("YES\n")
# else:
#     sys.stdout.write("NO\n")

n = int(input())
lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

for lucky_num in lucky_numbers:
    if n % lucky_num == 0:
        print("YES")
        exit()

print("NO")