def quitar_letra(l, s):
    for i in range(len(s)):
        if s[i] == l:
            s.pop(i)
            return s


# ne = ['A', 'B', 'C']
# letras = []
# for i in  range(len(s)):
#     if s[i] in ne:
#         letras.append(s[i])
# if len(letras) == 3:
#     print('Yes')
# else:
#     print('No')
s =list(map(str, input()))
res = 0
for char in s:
    if char == 'A':
        res += 1
        break
for char in s:
    if char == 'B':
        res += 1
        break
for char in s:
    if char == 'C':
        res += 1
        break
if res == 3:
    print('Yes')
else:
    print('No')
 

