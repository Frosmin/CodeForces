import sys


input_data = sys.stdin.read().split()


iterator = iter(input_data)


t = int(next(iterator))

for _ in range(t):

    n = int(next(iterator))

    if n == 1:
        print("1")
        continue
    results = []
    lim = (n - 3) // 2

    for i in range(lim + 1):
        zeros_i = "0" * i                  
        zeros_end = "0" * (n - 3 - 2 * i) 
        
        results.append(f"1{zeros_i}6{zeros_i}9{zeros_end}")
    for i in range(lim + 1):
        zeros_i = "0" * i
        zeros_end = "0" * (n - 3 - 2 * i)
        

        results.append(f"9{zeros_i}6{zeros_i}1{zeros_end}")

    results.append("196" + "0" * (n - 3))
    print('\n'.join(results))