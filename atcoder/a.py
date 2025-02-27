def opueto(item):
    if item == 'N':
        return 'S'
    elif item == 'S':
        return 'N'
    elif item == 'E':
        return 'W'
    else:
        return 'E'




d = list(map(str,input()))
for i in range(len(d)):
    d[i] = opueto(d[i])
print(''.join(d))
