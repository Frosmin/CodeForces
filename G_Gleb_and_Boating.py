def max_power():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    for _ in range(t):
        s = int(data[idx])
        k = int(data[idx+1])
        idx += 2
        
        if s % k == 0:
            print(k)
            continue
        
        current_pos = 0
        current_dir = 1  # 1 for forward, -1 for backward
        turns = 0
        power = k
        
        while True:
            if current_pos == s:
                break
            if current_dir == 1:
                available = s - current_pos
                steps = available // power
                if steps == 0:
                    steps = 1
                new_pos = current_pos + steps * power
                # Check if new_pos exceeds s
                if new_pos > s:
                    steps = (s - current_pos) // power
                    new_pos = current_pos + steps * power
                    if steps == 0:
                        steps = 1
                        new_pos = current_pos + power
                        if new_pos > s:
                            new_pos = s  # Force to s, but this should not happen
                current_pos = new_pos
            else:
                available = current_pos
                steps = available // power
                if steps == 0:
                    steps = 1
                new_pos = current_pos - steps * power
                # Check if new_pos goes below 0
                if new_pos < 0:
                    steps = current_pos // power
                    new_pos = current_pos - steps * power
                    if steps == 0:
                        steps = 1
                        new_pos = current_pos - power
                        if new_pos < 0:
                            new_pos = 0  # Force to 0, but this should not happen
                current_pos = new_pos
            
            if current_pos == s:
                break
            
            turns += 1
            power = max(power - 1, 1)
            current_dir *= -1
        
        print(max(k - turns, 1))

max_power()