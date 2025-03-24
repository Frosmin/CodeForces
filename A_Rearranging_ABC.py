def quitar_letra(l, s):
    for i in range(len(s)):
        if s[i] == l:
            s.pop(i)
            return s

s =list(map(str, input()))
ne = ['A', 'B', 'C']
letras = []
for i in  range(len(s)):
    if s[i] in ne:
        letras.append(s[i])
if len(letras) == 3:
    print('Yes')
else:
    print('No')

