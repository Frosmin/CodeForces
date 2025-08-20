
def buscar_palabra(palabra, dic):
    if palabra in dic:
       dic[palabra] += 1
       return f"{palabra}{dic[palabra]}"
    else:
        dic[palabra] = 0
        return "OK"




n = int(input())
dic = {}
for _ in range(n):
    palabra = input()
    print(buscar_palabra(palabra, dic))