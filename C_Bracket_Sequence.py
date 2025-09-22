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

def sumas (lst,n):
    new_list = []
    sumita = 0

    for i in range(n):
        if i != n:
            if lst[i] != '(' and lst[i] != ')':
                sumita += int(lst[i])
            else:
                new_list.append(sumita)
                sumita = 0
                new_list.append(lst[i])
    if sumita != 0 :
        new_list.append(sumita)
    return new_list




n  = int(input())
lst = list(map(str, input().split()[:n]))

print(sumas(lst,n))
