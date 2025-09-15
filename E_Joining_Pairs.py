# import sys
# input = sys.stdin.readline


# def an(x, y, id, w, h, lista):
#     if y == 0:
#         lista[0].append((x, id))
#         return 1
#     elif x == w:
#         lista[1].append((y, id))
#         return 1
#     elif y == h:
#         lista[2].append((-x, id))
#         return 1
#     elif x == 0:
#         lista[3].append((-y, id))
#         return 1
#     return 0



# w, h = map(int, input().split())
# n = int(input())
# # 0: abajo, 1: derecha, 2: arriba, 3: izquierd

# lista = [[] for _ in range(4)]

# freq = [0] * n

# for i in range(n):
    
#     a, b, c, d = map(int, input().split())
#     freq[i] += an(a, b, i, w, h, lista)
#     freq[i] += an(c, d, i, w, h, lista)
    

# a = []
# for i in range(4):
#     lista[i].sort()
#     a.extend(lista[i])
    
# st = []  
# cnt = [0] * n 

# for _, x_id in a:
#     if freq[x_id] != 2:
#         continue
        
#     cnt[x_id] += 1
#     if cnt[x_id] == 2:
#         if not st or st[-1] != x_id:
#             print("N")
#             exit()
#         st.pop() 
#     else: 
#         st.append(x_id) 
        

# if not st:
#     print("Y")
# else:
#     print("N")

import sys

def main():


    sides = [[] for _ in range(4)]
    freq = [0] * n  

    def add_endpoint(x, y, idx):
        if y == 0:
            sides[0].append((x, idx)); return 1
        if x == w:
            sides[1].append((y, idx)); return 1
        if y == h:
            sides[2].append((-x, idx)); return 1  
        if x == 0:
            sides[3].append((-y, idx)); return 1  
        return 0 

    for i in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        freq[i] += add_endpoint(x1, y1, i)
        freq[i] += add_endpoint(x2, y2, i)

    order = []
    for s in range(4):
        if sides[s]:
            sides[s].sort()
            order.extend(sides[s])

    stack = []
    seen = [0] * n

    for _, idx in order:
        if freq[idx] != 2:
            continue  
        seen[idx] += 1
        if seen[idx] == 1:
            stack.append(idx)
        else:
            if not stack or stack[-1] != idx:
                print("N")
                return
            stack.pop()

    print("Y" if not stack else "N")

    input = sys.stdin.readline
    w, h = map(int, input().split())
    n = int(input())