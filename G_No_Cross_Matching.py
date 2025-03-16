# def do_segments_intersect(p1, q1, p2, q2):
#     """
#     Verifica si dos segmentos se intersectan.
#     p1, q1: puntos del primer segmento
#     p2, q2: puntos del segundo segmento
#     """
#     def orientation(p, q, r):
#         val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
#         if val == 0:
#             return 0  # colinear
#         return 1 if val > 0 else 2  # en sentido horario o antihorario
    
#     def on_segment(p, q, r):
#         return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
#                 q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))
    
#     # Orientaciones
#     o1 = orientation(p1, q1, p2)
#     o2 = orientation(p1, q1, q2)
#     o3 = orientation(p2, q2, p1)
#     o4 = orientation(p2, q2, q1)
    
#     # Caso general de intersección
#     if o1 != o2 and o3 != o4:
#         return True
    
#     # Casos especiales (colineales)
#     if o1 == 0 and on_segment(p1, p2, q1): return True
#     if o2 == 0 and on_segment(p1, q2, q1): return True
#     if o3 == 0 and on_segment(p2, p1, q2): return True
#     if o4 == 0 and on_segment(p2, q1, q2): return True
    
#     return False

# def solve_no_cross_matching():
#     n = int(input())
    
#     # Leer coordenadas de los puntos P
#     p_points = []
#     for _ in range(n):
#         a, b = map(int, input().split())
#         p_points.append((a, b))
    
#     # Leer coordenadas de los puntos Q
#     q_points = []
#     for _ in range(n):
#         c, d = map(int, input().split())
#         q_points.append((c, d))
    
#     # La solución greedy con ordenamiento no garantiza una solución correcta
#     # Usamos directamente el backtracking que sí garantiza la respuesta correcta
    
#     R = [0] * n
#     used = [False] * n
    
#     def backtrack(index):
#         if index == n:
#             return True
        
#         # Verificar cada posible asignación para el punto P_index
#         for i in range(n):
#             if not used[i]:
#                 valid = True
#                 R[index] = i + 1
#                 used[i] = True
                
#                 # Verificar si hay cruces con segmentos anteriores
#                 for j in range(index):
#                     if do_segments_intersect(
#                         p_points[j], q_points[R[j]-1],
#                         p_points[index], q_points[R[index]-1]
#                     ):
#                         valid = False
#                         break
                
#                 if valid and backtrack(index + 1):
#                     return True
                
#                 used[i] = False
        
#         return False
    
#     # Ejecutamos el algoritmo de backtracking
#     if backtrack(0):
#         return " ".join(map(str, R))
    
#     return "-1"

# print(solve_no_cross_matching())



# def do_segments_intersect(p1, q1, p2, q2):
#     """
#     Verifica si dos segmentos se intersectan.
#     p1, q1: puntos del primer segmento
#     p2, q2: puntos del segundo segmento
#     """
#     def orientation(p, q, r):
#         val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
#         if val == 0:
#             return 0  # colinear
#         return 1 if val > 0 else 2  # en sentido horario o antihorario
    
#     def on_segment(p, q, r):
#         return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
#                 q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))
    
#     # Orientaciones
#     o1 = orientation(p1, q1, p2)
#     o2 = orientation(p1, q1, q2)
#     o3 = orientation(p2, q2, p1)
#     o4 = orientation(p2, q2, q1)
    
#     # Caso general de intersección
#     if o1 != o2 and o3 != o4:
#         return True
    
#     # Casos especiales (colineales)
#     if o1 == 0 and on_segment(p1, p2, q1): return True
#     if o2 == 0 and on_segment(p1, q2, q1): return True
#     if o3 == 0 and on_segment(p2, p1, q2): return True
#     if o4 == 0 and on_segment(p2, q1, q2): return True
    
#     return False

# def solve_no_cross_matching():
#     import sys
#     input = sys.stdin.read
#     data = input().split()
    
#     n = int(data[0])
#     p_points = []
#     q_points = []
    
#     index = 1
#     for i in range(n):
#         a, b = int(data[index]), int(data[index + 1])
#         p_points.append((a, b))
#         index += 2
    
#     for i in range(n):
#         c, d = int(data[index]), int(data[index + 1])
#         q_points.append((c, d))
#         index += 2
    
#     R = [0] * n
#     used = [False] * n
    
#     def backtrack(index):
#         if index == n:
#             return True
        
#         for i in range(n):
#             if not used[i]:
#                 valid = True
#                 R[index] = i + 1
#                 used[i] = True
                
#                 for j in range(index):
#                     if do_segments_intersect(
#                         p_points[j], q_points[R[j]-1],
#                         p_points[index], q_points[R[index]-1]
#                     ):
#                         valid = False
#                         break
                
#                 if valid and backtrack(index + 1):
#                     return True
                
#                 used[i] = False
        
#         return False
    
#     if backtrack(0):
#         print(" ".join(map(str, R)))
#     else:
#         print("-1")
import math

def ccw(A, B, C):
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])

def segments_intersect(A, B, C, D):
    ccw1 = ccw(A, B, C)
    ccw2 = ccw(A, B, D)
    if ccw1 * ccw2 > 0:
        return False
    ccw3 = ccw(C, D, A)
    ccw4 = ccw(C, D, B)
    if ccw3 * ccw4 > 0:
        return False
    return True

def is_valid(P, Q, R):
    for i in range(len(R)):
        for j in range(i + 1, len(R)):
            A = P[i]
            B = Q[R[i] - 1]
            C = P[j]
            D = Q[R[j] - 1]
            if segments_intersect(A, B, C, D):
                return False
    return True

def generate_candidates(P, Q, N):
    candidates = []

    def create_R(sorted_p_indices, sorted_q_indices):
        pos_p = [0] * N
        for idx, i in enumerate(sorted_p_indices):
            pos_p[i] = idx
        R = [sorted_q_indices[pos_p[i]] + 1 for i in range(N)]
        return R

    # Sorting by x, then y for both P and Q
    sorted_p_x = sorted(range(N), key=lambda i: (P[i][0], P[i][1]))
    sorted_q_x = sorted(range(N), key=lambda i: (Q[i][0], Q[i][1]))
    R_x = create_R(sorted_p_x, sorted_q_x)
    candidates.append(R_x)

    # Sorting by y, then x for both P and Q
    sorted_p_y = sorted(range(N), key=lambda i: (P[i][1], P[i][0]))
    sorted_q_y = sorted(range(N), key=lambda i: (Q[i][1], Q[i][0]))
    R_y = create_R(sorted_p_y, sorted_q_y)
    candidates.append(R_y)

    # Sorting by x + y
    sorted_p_xy = sorted(range(N), key=lambda i: (P[i][0] + P[i][1]))
    sorted_q_xy = sorted(range(N), key=lambda i: (Q[i][0] + Q[i][1]))
    R_xy = create_R(sorted_p_xy, sorted_q_xy)
    candidates.append(R_xy)

    # Sorting by x - y
    sorted_p_xmy = sorted(range(N), key=lambda i: (P[i][0] - P[i][1]))
    sorted_q_xmy = sorted(range(N), key=lambda i: (Q[i][0] - Q[i][1]))
    R_xmy = create_R(sorted_p_xmy, sorted_q_xmy)
    candidates.append(R_xmy)

    # Sorting by angle around centroid
    sum_x = sum(p[0] for p in P) + sum(q[0] for q in Q)
    sum_y = sum(p[1] for p in P) + sum(q[1] for q in Q)
    cent_x = sum_x / (2 * N)
    cent_y = sum_y / (2 * N)

    def get_angle(point):
        return math.atan2(point[1] - cent_y, point[0] - cent_x)

    sorted_p_angle = sorted(range(N), key=lambda i: get_angle(P[i]))
    sorted_q_angle = sorted(range(N), key=lambda i: get_angle(Q[i]))
    R_angle = create_R(sorted_p_angle, sorted_q_angle)
    candidates.append(R_angle)

    return candidates

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1

    P = []
    for _ in range(N):
        x = int(input[ptr])
        y = int(input[ptr + 1])
        P.append((x, y))
        ptr += 2

    Q = []
    for _ in range(N):
        x = int(input[ptr])
        y = int(input[ptr + 1])
        Q.append((x, y))
        ptr += 2

    candidates = generate_candidates(P, Q, N)

    for R in candidates:
        if is_valid(P, Q, R):
            print(' '.join(map(str, R)))
            return

    print(-1)

if __name__ == '__main__':
    main()