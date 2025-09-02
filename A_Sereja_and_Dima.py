n = int(input())
lst = list(map(int,input().split()))
a,b= 0,0

bb = True

for i in range(n):
    inicio = lst[0]
    fin = lst[-1]
    if bb ==True:
        if inicio >= fin:
            a+=inicio
            lst.pop(0)
            bb = False
        else:
            a+=fin
            lst.pop()
            bb = False
    else:
        if inicio >= fin:
            b+=inicio
            lst.pop(0)
            bb = True
        else:
            b+=fin
            lst.pop()
            bb = True
print(a ,b)