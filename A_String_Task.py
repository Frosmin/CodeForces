def quitar_vocales(palabra):
    nueva_palabra = ""
 
    for letra in palabra:
        if letra == 'a' or letra == 'e'  or  letra == 'i'or  letra == 'o' or  letra == 'u'or letra == 'y':
            pass
        else:
            nueva_palabra +=letra       
    return nueva_palabra
            
palabra = input().strip().casefold()
res = quitar_vocales(palabra)
 
res = '.'.join(res)
print('.'+res)