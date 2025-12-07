import sys
from collections import Counter



input_data = sys.stdin.read().split()
iterator = iter(input_data)

t = int(next(iterator))
for _ in range(t):
    n = int(next(iterator))
    
    elements = [int(next(iterator)) for _ in range(n)]
    mp = Counter(elements)
    
    res = []
    
    sorted_keys = sorted(mp.keys())
    
    for num in sorted_keys:
        cant = mp[num] // 2
        if cant > 0:
            res.extend([num] * cant)
    
    if len(res) < 4:
        print("NO")
    else:
        v1 = res[0]
        v2 = res[1]
        v4 = res[-1]
        v3 = res[-2]
        
        print("YES")
        print(f"{v1} {v2} {v1} {v4} {v3} {v2} {v3} {v4}")