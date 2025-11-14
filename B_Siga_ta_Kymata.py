import sys

def main():
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    index = 1
    output_lines = []
    for _ in range(t):
        n = int(data[index]); index += 1
        p = list(map(int, data[index].split())); index += 1
        x_str = data[index].strip(); index += 1
        

        left_smaller = [False] * n
        left_larger = [False] * n
        right_smaller = [False] * n
        right_larger = [False] * n
        

        if n > 0:
            pre_min = p[0]
            pre_max = p[0]
            for i in range(1, n):
                if pre_min < p[i]:
                    left_smaller[i] = True
                if pre_max > p[i]:
                    left_larger[i] = True
                pre_min = min(pre_min, p[i])
                pre_max = max(pre_max, p[i])
                

            suf_min = p[n-1]
            suf_max = p[n-1]
            for i in range(n-2, -1, -1):
                if suf_min < p[i]:
                    right_smaller[i] = True
                if suf_max > p[i]:
                    right_larger[i] = True
                suf_min = min(suf_min, p[i])
                suf_max = max(suf_max, p[i])
                

        possible = True
        for i in range(n):
            if x_str[i] == '1':
                coverable = (left_smaller[i] and right_larger[i]) or (left_larger[i] and right_smaller[i])
                if not coverable:
                    output_lines.append(str(-1))
                    possible = False
                    break
                    
        if not possible:
            continue
            

        min_val = min(p)
        max_val = max(p)
        a_index = 0
        b_index = 0
        for i in range(n):
            if p[i] == min_val:
                a_index = i+1
            if p[i] == max_val:
                b_index = i+1
                
        L = min(a_index, b_index)
        R = max(a_index, b_index)
        
        left_needed = False
        for i in range(1, L):
            if x_str[i-1] == '1':
                left_needed = True
                break
                
        right_needed = False
        for i in range(R+1, n+1):
            if x_str[i-1] == '1':
                right_needed = True
                break
                
        mid_needed = False
        for i in range(L+1, R):
            if x_str[i-1] == '1':
                mid_needed = True
                break
                
        operations_set = set()
        if left_needed:
            if a_index > 1:
                operations_set.add((1, a_index))
            if b_index > 1:
                operations_set.add((1, b_index))
                
        if mid_needed:
            if R - L > 1:
                operations_set.add((L, R))
                
        if right_needed:
            if a_index < n:
                operations_set.add((a_index, n))
            if b_index < n:
                operations_set.add((b_index, n))
                
        k = len(operations_set)
        output_lines.append(str(k))
        for op in sorted(operations_set):
            output_lines.append(f"{op[0]} {op[1]}")
            
    sys.stdout.write("\n".join(output_lines))
    
if __name__ == "__main__":
    main()