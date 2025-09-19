import sys



n_str = sys.stdin.readline()
n = int(n_str)


values_str = sys.stdin.readline().split()
variables = {}
for i in range(n):
    char_code = ord('A') + i
    variable_char = chr(char_code)
    variables[variable_char] = (values_str[i] == 'T')
expression = sys.stdin.readline().split()
stack = []
for token in expression:
    if 'A' <= token <= 'Z':
        stack.append(variables[token])
    else:
        if token == '*':  
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 and op2)
        elif token == '+':  
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 or op2)
        elif token == '-':  
            op1 = stack.pop()
            stack.append(not op1)
result = stack[0]
if result:
    print('T')
else:
    print('F')