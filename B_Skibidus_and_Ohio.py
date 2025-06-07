# n = int(input())
# res = 0
# for _ in range(n):
#     lista = list(map(str, input()))
#     res = 0
#     for i in range(len(lista)):
        
#         if i == len(lista) - 1:
#             break
#         if lista[i] == lista[i+1]:
#             res += 1
#     if res == 0:
#         print(len(lista))
#     else:
#         print(res)      
            


n = int(input())

for _ in range(n):
    s = list(input()) 
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:  
            if i > 0:
                s[i] = s[i - 1]
            else:
                s[i] = 'a'
            s.pop(i + 1)
            i = max(0, i - 1)
        else:
            i += 1
    print(len(s))