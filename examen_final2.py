n = int(input())
lstx = []
lsty = []
min_x = 100001
max_x = -100001
min_y = 100001
max_y = -100001

for _ in range(n):
    x,y = map(int,input().split())

    if x < min_x: min_x = x
    if x > max_x: max_x = x
    if y < min_y: min_y = y
    if y > max_y: max_y = y

res_x = (min_x + max_x) / 2
res_y = (min_y + max_y) / 2


print(f"{res_x:.2f} {res_y:.2f}")