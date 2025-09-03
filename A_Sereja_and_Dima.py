n = int(input())
lst = list(map(int,input().split()))
a,b= 0,0

for i in range(n):
    inicio = lst[0]
    fin = lst[-1]
    if i%2 ==0:
        if inicio >= fin:
            a+=inicio
            lst.pop(0)
        else:
            a+=fin
            lst.pop()
    else:
        if inicio >= fin:
            b+=inicio
            lst.pop(0)
        else:
            b+=fin
            lst.pop()
print(a ,b)