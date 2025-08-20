def quitar_vocales(word):
    nueva_word = ""
    word=word.lower()
    for letra in word:
        if letra == 'a' or letra == 'e'  or  letra == 'i'or  letra == 'o' or  letra == 'u'or letra == 'y':
            pass
        else:
            nueva_word +=letra       
    return nueva_word
            
word = input()
res = quitar_vocales(word)

res = '.'.join(res)
print('.'+res)



def quitar_vocales(word):
    nueva_word = ""
    for letra in word:
        if letra == 'a' or letra == 'e'  or  letra == 'i'or  letra == 'o' or  letra == 'u'or letra == 'y':
            pass
        else:
            nueva_word +=letra       
    return nueva_word
            
word = input().strip().casefold()
res = quitar_vocales(word)

res = '.'.join(res)
print('.'+res)


def quitar_vocales(word):
    vocales = set('aeiouy')
    return '.'.join(ch for ch in word if ch not in vocales)

word = input().strip().casefold()
res = quitar_vocales(word)
print('.' + res)