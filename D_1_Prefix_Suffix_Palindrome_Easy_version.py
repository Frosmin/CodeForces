# filepath: 
import sys


sys.setrecursionlimit(2000)

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
    

    middle = s[l : r+1]
    

    longest_prefix_pal = ""

    for i in range(len(middle), 0, -1):
        sub = middle[:i]
        if sub == sub[::-1]:
            longest_prefix_pal = sub
            break
            

    longest_suffix_pal = ""

    for i in range(len(middle), 0, -1):
        sub = middle[len(middle)-i:]
        if sub == sub[::-1]:
            longest_suffix_pal = sub
            break
            

    if len(longest_prefix_pal) >= len(longest_suffix_pal):
        print(prefix_part + longest_prefix_pal + suffix_part)
    else:
        print(prefix_part + longest_suffix_pal + suffix_part)

input_line = sys.stdin.readline().strip()
t = int(input_line)
for _ in range(t):
    solve()
