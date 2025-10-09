# import sys
# from collections import deque

# def main():
#     data = sys.stdin.read().split()
#     if not data:
#         return
    
#     it = iter(data)
#     n = int(next(it)); q = int(next(it))
#     maxn = 300005
#     bsz = 500
    
#     id_arr = list(range(maxn))
#     nid = [0] * maxn
#     del_arr = [False] * maxn
#     stksz = 0
#     sl = [0] * maxn
#     sr = [0] * maxn
#     rv = [False] * maxn
#     que_arr = [deque() for _ in range(maxn)]
#     my = [deque() for _ in range(maxn)]
    
#     def add_segment(l, r, bl, q_deque):
#         nonlocal stksz
#         stksz += 1
#         sl[stksz] = l
#         sr[stksz] = r
#         rv[stksz] = bl
#         que_arr[stksz] = deque(q_deque)
    
#     def segment_length(i):
#         return sr[i] - sl[i] + 1
    
#     def flip_segment(i):
#         rv[i] = not rv[i]
    
#     def reverse_segments(ord_list, x):
#         total = 0
#         for i, seg_idx in enumerate(ord_list):
#             total += segment_length(seg_idx)
#             if total == x:
#                 new_ord = ord_list[:i+1]
#                 new_ord.reverse()
#                 for j in range(i+1):
#                     flip_segment(ord_list[j])
#                 new_ord.extend(ord_list[i+1:])
#                 return new_ord
#         assert False, "Reverse operation failed"
    
#     def cut_segments(ord_list, x):
#         total = 0
#         for i, seg_idx in enumerate(ord_list):
#             seg_len = segment_length(seg_idx)
#             total += seg_len
#             if total == x:
#                 return ord_list
#             if total > x:
#                 total -= seg_len
#                 new_ord = ord_list[:i]
#                 current_seg = ord_list[i]
#                 if not rv[current_seg]:
#                     l1 = sl[current_seg]
#                     r1 = sl[current_seg] + (x - total) - 1
#                     l2 = sl[current_seg] + (x - total)
#                     r2 = sr[current_seg]
#                     assert l2 <= r2, "Invalid segment division"
#                     add_segment(l1, r1, False, que_arr[current_seg])
#                     new_ord.append(stksz)
#                     add_segment(l2, r2, False, que_arr[current_seg])
#                     new_ord.append(stksz)
#                 else:
#                     l1 = sr[current_seg] - (x - total - 1)
#                     r1 = sr[current_seg]
#                     l2 = sl[current_seg]
#                     r2 = sr[current_seg] - (x - total)
#                     assert l2 <= r2, "Invalid segment division"
#                     add_segment(l1, r1, True, que_arr[current_seg])
#                     new_ord.append(stksz)
#                     add_segment(l2, r2, True, que_arr[current_seg])
#                     new_ord.append(stksz)
#                 new_ord.extend(ord_list[i+1:])
#                 return new_ord
#         assert False, "Cut operation failed"
    
#     def solve_value(p):
#         while my[p]:
#             seg_idx = my[p][0]
#             while que_arr[seg_idx]:
#                 v = que_arr[seg_idx][0]
#                 if del_arr[v]:
#                     que_arr[seg_idx].popleft()
#                 else:
#                     return v
#             my[p].popleft()
#         return 0
    
#     ans = 0
#     for bid in range(0, (q + bsz - 1) // bsz):
#         ql = bid * bsz + 1
#         qr = min(q, (bid + 1) * bsz)
#         if ql > qr:
#             break
            
#         segments_order = []
#         add_segment(1, n, False, deque())
#         segments_order.append(stksz)
        
#         for qid in range(ql, qr + 1):
#             a = int(next(it)); b = int(next(it)); c = int(next(it))
#             if a == 1:
#                 r = (b + ans - 1) % n + 1
#                 segments_order = cut_segments(segments_order, r)
#                 current_total = 0
#                 for seg in segments_order:
#                     seg_len = segment_length(seg)
#                     if current_total + seg_len <= r:
#                         que_arr[seg].append(qid)
#                         current_total += seg_len
#                     else:
#                         break
#             elif a == 2:
#                 r = (b + ans - 1) % n + 1
#                 segments_order = cut_segments(segments_order, r)
#                 segments_order = reverse_segments(segments_order, r)
#             elif a == 3:
#                 x = (b + ans - 1) % q + 1
#                 if x <= qid:
#                     del_arr[x] = True
                    
#             p_val = (c + ans - 1) % n + 1
#             total_len = 0
#             found_val = -1
#             for seg in segments_order:
#                 seg_len = segment_length(seg)
#                 if total_len + seg_len >= p_val:
#                     if not rv[seg]:
#                         pos = sl[seg] + (p_val - total_len - 1)
#                         found_val = id_arr[pos]
#                     else:
#                         pos = sr[seg] - (p_val - total_len - 1)
#                         found_val = id_arr[pos]
#                     break
#                 total_len += seg_len
                
#             ans = solve_value(found_val)
#             if ans == 0:
#                 total_len = 0
#                 for seg in segments_order:
#                     seg_len = segment_length(seg)
#                     if total_len + seg_len >= p_val:
#                         while que_arr[seg]:
#                             v = que_arr[seg][0]
#                             if del_arr[v]:
#                                 que_arr[seg].popleft()
#                             else:
#                                 ans = v
#                                 break
#                         break
#                     total_len += seg_len
                    
#             print(ans)
            
#         tsz = 1
#         for seg in segments_order:
#             l = sl[seg]; r = sr[seg]; reverse = rv[seg]
#             if not reverse:
#                 for i in range(l, r + 1):
#                     my[id_arr[i]].append(seg)
#                     nid[tsz] = id_arr[i]
#                     tsz += 1
#             else:
#                 for i in range(r, l - 1, -1):
#                     my[id_arr[i]].append(seg)
#                     nid[tsz] = id_arr[i]
#                     tsz += 1
                    
#         for i in range(1, n + 1):
#             id_arr[i] = nid[i]
            
# if __name__ == "__main__":
#     main()

import sys

# Constantes
M = 300000
Q = 300000
N_ = 1 << 19  # N_ = pow2(ceil(log2(Q + 1)))

# Variables globales
m = 0
q = 0
n_ = 0

# Arreglos para almacenar consultas
type_arr = [0] * Q
xx_arr = [0] * Q

def alloc(n):
    return [0] * n

def pul(u):
    # Buffers temporales
    xx_temp = [0] * (M + 1)
    kkl = [0] * (M + 1)
    kkr = [0] * (M + 1)
    jj_temp = [0] * (M + 1)
    
    l = u << 1
    r = l | 1
    i = 0
    j = 0
    k = 0
    
    # Combinar puntos de corte
    while i <= nn[l] and j <= nn[r]:
        x = min(xxr[l][i], xxl[r][j])
        xx_temp[k] = x
        if xxr[l][i] == x:
            kkl[i] = k
            i += 1
        if xxl[r][j] == x:
            kkr[j] = k
            j += 1
        k += 1
    
    nn[u] = k - 1
    xxr[u] = alloc(nn[u] + 1)
    ppr[u] = alloc(nn[u])
    jjl[r] = alloc(nn[r])
    jjr[r] = alloc(nn[r])
    
    j_ = 0
    for j in range(nn[r]):
        j1 = aar[r][j] >> 1
        kl = kkr[j1]
        kr = kkr[j1 + 1]
        jjl[r][j] = j_
        
        if (aar[r][j] & 1) == 0:
            for k in range(kl, kr):
                jj_temp[k] = j_ << 1 | 0
                ppr[u][j_] = j
                xxr[u][j_] = xxr[r][j] + xx_temp[k] - xx_temp[kl]
                j_ += 1
        else:
            for k in range(kr - 1, kl - 1, -1):
                jj_temp[k] = j_ << 1 | 1
                ppr[u][j_] = j
                xxr[u][j_] = xxr[r][j] + xx_temp[kr] - xx_temp[k + 1]
                j_ += 1
        jjr[r][j] = j_
    
    xxr[u][nn[u]] = m
    xxl[u] = alloc(nn[u] + 1)
    aal[u] = alloc(nn[u])
    aar[u] = alloc(nn[u])
    ppl[u] = alloc(nn[u])
    on[u] = alloc(nn[u])
    jjl[l] = alloc(nn[l])
    jjr[l] = alloc(nn[l])
    
    i_ = 0
    for i in range(nn[l]):
        i1 = aal[l][i] >> 1
        kl = kkl[i1]
        kr = kkl[i1 + 1]
        jjl[l][i1] = i_
        
        if (aal[l][i] & 1) == 0:
            for k in range(kl, kr):
                j_ = jj_temp[k] >> 1
                if (jj_temp[k] & 1) == 0:
                    aal[u][i_] = j_ << 1 | 0
                    aar[u][j_] = i_ << 1 | 0
                else:
                    aal[u][i_] = j_ << 1 | 1
                    aar[u][j_] = i_ << 1 | 1
                ppl[u][j_] = i1
                on[u][j_] = 1 if (on[l][ppl[u][j_]] or on[r][ppr[u][j_]]) else 0
                xxl[u][i_] = xxl[l][i] + xx_temp[k] - xx_temp[kl]
                i_ += 1
        else:
            for k in range(kr - 1, kl - 1, -1):
                j_ = jj_temp[k] >> 1
                if (jj_temp[k] & 1) == 0:
                    aal[u][i_] = j_ << 1 | 1
                    aar[u][j_] = i_ << 1 | 1
                else:
                    aal[u][i_] = j_ << 1 | 0
                    aar[u][j_] = i_ << 1 | 0
                ppl[u][j_] = i1
                on[u][j_] = 1 if (on[l][ppl[u][j_]] or on[r][ppr[u][j_]]) else 0
                xxl[u][i_] = xxl[l][i] + xx_temp[kr] - xx_temp[k + 1]
                i_ += 1
        jjr[l][i1] = i_
    
    xxl[u][nn[u]] = m

def add(h):
    u = n_ + h
    
    if type_arr[h] == 1:
        nn[u] = 1 if xx_arr[h] == m else 2
        xxl[u] = alloc(nn[u] + 1)
        xxr[u] = alloc(nn[u] + 1)
        aal[u] = alloc(nn[u])
        aar[u] = alloc(nn[u])
        on[u] = alloc(nn[u])
        
        xxl[u][0] = 0
        xxr[u][0] = 0
        xxl[u][1] = xx_arr[h]
        xxr[u][1] = xx_arr[h]
        aal[u][0] = 0 << 1 | 0
        aar[u][0] = 0 << 1 | 0
        on[u][0] = 1
        
        if xx_arr[h] < m:
            xxl[u][2] = m
            xxr[u][2] = m
            aal[u][1] = 1 << 1 | 0
            aar[u][1] = 1 << 1 | 0
            on[u][1] = 0
    
    elif type_arr[h] == 2:
        nn[u] = 1 if xx_arr[h] == m else 2
        xxl[u] = alloc(nn[u] + 1)
        xxr[u] = alloc(nn[u] + 1)
        aal[u] = alloc(nn[u])
        aar[u] = alloc(nn[u])
        on[u] = alloc(nn[u])
        
        xxl[u][0] = 0
        xxr[u][0] = 0
        xxl[u][1] = xx_arr[h]
        xxr[u][1] = xx_arr[h]
        aal[u][0] = 0 << 1 | 1
        aar[u][0] = 0 << 1 | 1
        on[u][0] = 0
        
        if xx_arr[h] < m:
            xxl[u][2] = m
            xxr[u][2] = m
            aal[u][1] = 1 << 1 | 0
            aar[u][1] = 1 << 1 | 0
            on[u][1] = 0
    
    else:
        nn[u] = 1
        xxl[u] = alloc(nn[u] + 1)
        xxr[u] = alloc(nn[u] + 1)
        aal[u] = alloc(nn[u])
        aar[u] = alloc(nn[u])
        on[u] = alloc(nn[u])
        
        xxl[u][0] = 0
        xxr[u][0] = 0
        xxl[u][1] = m
        xxr[u][1] = m
        aal[u][0] = 0 << 1 | 0
        aar[u][0] = 0 << 1 | 0
        on[u][0] = 0
    
    # Propagar hacia arriba mientras sea hijo derecho
    while u > 1 and (u & 1) != 0:
        u >>= 1
        pul(u)

def purge(u, i):
    on[u][i] = 0
    if jjl[u] is None:
        return
    
    v = u >> 1
    l = v << 1
    r = l | 1
    
    for j in range(jjl[u][i], jjr[u][i]):
        j_ = j if (u & 1) != 0 else aal[v][j] >> 1
        if not on[l][ppl[v][j_]] and not on[r][ppr[v][j_]]:
            purge(v, j_)

def search(u, x):
    lower = 0
    upper = nn[u]
    
    while upper - lower > 1:
        j = (lower + upper) // 2
        
        if xxr[u][j] <= x:
            lower = j
        else:
            upper = j
    
    return lower

def query(r, x):
    l = 0
    u = -1
    j_ = -1
    
    L = l + n_
    R = r + n_
    
    while L <= R:
        if (R & 1) == 0:
            j = search(R, x)
            if on[R][j]:
                u = R
                j_ = j
            i = aar[R][j] >> 1
            if (aar[R][j] & 1) == 0:
                x = xxl[R][i] + x - xxr[R][j]
            else:
                x = xxl[R][i + 1] - 1 - (x - xxr[R][j])
            R -= 1
        L >>= 1
        R >>= 1
    
    if u == -1:
        return 0
    
    j = j_
    while u < n_:
        if on[u << 1 | 0][ppl[u][j]]:
            j = ppl[u][j]
            u = u << 1 | 0
        else:
            j = ppr[u][j]
            u = u << 1 | 1
    
    return u - n_ + 1

def main():
    global m, q, n_
    global nn, xxl, xxr, aal, aar, on, jjl, jjr, ppl, ppr
    global type_arr, xx_arr
    
    # Leer toda la entrada de una vez para mejorar rendimiento
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    
    m = next(it)
    q = next(it)
    
    # Calcular potencia de 2 mayor o igual a q
    n_ = 1
    while n_ <= q:
        n_ <<= 1
    
    # Inicializar estructuras de datos
    size = 2 * n_
    nn = [0] * size
    xxl = [None] * size
    xxr = [None] * size
    aal = [None] * size
    aar = [None] * size
    on = [None] * size
    jjl = [None] * size
    jjr = [None] * size
    ppl = [None] * size
    ppr = [None] * size
    
    ans = 0
    out_lines = []
    
    for h in range(q):
        type_arr[h] = next(it)
        xx_arr[h] = next(it) - 1
        x = next(it) - 1
        
        if type_arr[h] == 1 or type_arr[h] == 2:
            xx_arr[h] = (xx_arr[h] + ans) % m + 1
        else:
            xx_arr[h] = (xx_arr[h] + ans) % q
        
        add(h)
        
        if type_arr[h] == 3 and xx_arr[h] < h and type_arr[xx_arr[h]] == 1:
            type_arr[xx_arr[h]] = 0
            purge(n_ + xx_arr[h], 0)
        
        x = (x + ans) % m
        ans = query(h, x)
        out_lines.append(str(ans))
    
    # Imprimir resultados
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    # Aumentar límite de recursión para evitar stack overflow
    sys.setrecursionlimit(10000)
    main()