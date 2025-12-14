# n = int(input())
# lstx = []
# lsty = []
# min_x = 100001
# max_x = -100001
# min_y = 100001
# max_y = -100001

# for _ in range(n):
#     x,y = map(int,input().split())

#     if x < min_x: min_x = x
#     if x > max_x: max_x = x
#     if y < min_y: min_y = y
#     if y > max_y: max_y = y

# res_x = (min_x + max_x) / 2
# res_y = (min_y + max_y) / 2


# print(f"{res_x:.2f} {res_y:.2f}")

# import sys
# import math

# sys.setrecursionlimit(2000)

# input_data = sys.stdin.read().split()

# iterator = iter(input_data)

# n = int(next(iterator))

# xs = []
# ys = []

# for _ in range(n):
#     xs.append(int(next(iterator)))
#     ys.append(int(next(iterator)))
# curr_x = sum(xs) / n
# curr_y = sum(ys) / n
# num_iterations = 80  

# for _ in range(num_iterations):
#     numerator_x = 0.0
#     numerator_y = 0.0
#     denominator = 0.0
    
#     for i in range(n):
#         dx = xs[i] - curr_x
#         dy = ys[i] - curr_y
    
#         dist = math.sqrt(dx*dx + dy*dy)
        
#         if dist < 1e-7:
#             dist = 1e-7
            
#         weight = 1.0 / dist
        
#         numerator_x += xs[i] * weight
#         numerator_y += ys[i] * weight
#         denominator += weight
        
#     if denominator == 0:
#         break
        
#     curr_x = numerator_x / denominator
#     curr_y = numerator_y / denominator
# print(f"{curr_x:.2f} {curr_y:.2f}")



import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])

    xmin = ymin = float('inf')
    xmax = ymax = float('-inf')

    idx = 1
    for _ in range(n):
        x = float(data[idx])
        y = float(data[idx + 1])
        idx += 2

        xmin = min(xmin, x)
        xmax = max(xmax, x)
        ymin = min(ymin, y)
        ymax = max(ymax, y)

    cx = (xmin + xmax) / 2
    cy = (ymin + ymax) / 2

    print(f"{cx:.2f} {cy:.2f}")

if __name__ == "__main__":
    main()