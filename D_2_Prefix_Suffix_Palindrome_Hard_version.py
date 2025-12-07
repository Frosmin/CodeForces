
import sys



def mas_grande(t):
    temp = t + '#' + t[::-1]
    n = len(temp)
    pi = [0] * n
    

    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and temp[i] != temp[j]:
            j = pi[j-1]
        if temp[i] == temp[j]:
            j += 1
        pi[i] = j
    

    return t[:pi[-1]]

def solve():

    s = sys.stdin.readline().strip()
    if not s:
        return

    n = len(s)
    l, r = 0, n - 1
    

    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            break

    if l >= r:
        print(s)
        return
    

    prefix_part = s[:l]
    suffix_part = s[r+1:]
    

    mid = s[l : r+1]
    

    pal_prefix = mas_grande(mid)
    

    pal_suffix_str = mas_grande(mid[::-1])
    

    if len(pal_prefix) >= len(pal_suffix_str):
        print(prefix_part + pal_prefix + suffix_part)
    else:
        print(prefix_part + pal_suffix_str + suffix_part)



input_line = sys.stdin.readline().strip()
t = int(input_line)
for _ in range(t):
    solve()
