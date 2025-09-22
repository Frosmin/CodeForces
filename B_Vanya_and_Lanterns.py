


n,l = map(int, input().split()) #n faores y tam calle
lst = list(map(int,input().split()))
 


lst = sorted(set(lst))

new_list= []
maximo = 0

inicio = lst[0]
final = l - lst[-1] 

masgrande = max(inicio,final)



for i in range(len(lst)-1):
    tomate =  lst[i+1]-lst[i]
    if tomate>maximo:
        maximo = tomate


if masgrande > maximo/2:
    print(masgrande)
else:
    print(maximo/2)