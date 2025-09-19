mod = 10**9 + 7

n = int(input())
valores = input().split()

stack = []
op = 'add'
value = 0

for token in valores:
    if token == '(':
        stack.append((op, value))
        if op == 'add':
            op = 'mult'
            value = 1
        else:
            op = 'add'
            value = 0
    elif token == ')':
        prev_op, prev_val = stack.pop()
        if prev_op == 'add':
            value = (prev_val + value) % mod
        else:
            value = (prev_val * value) % mod
        op = prev_op
    else:
        num = int(token)
        if op == 'add':
            value = (value + num) % mod
        else:
            value = (value * num) % mod
            
print(value % mod)

