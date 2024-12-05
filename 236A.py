

name = list(map(str,input()))
if not(len(name) < 100):
     raise ValueError("error")

def existe(n, list):
    if list == []:
        return False
    for i in range(len(list)):
        if n == list[i]:
            return True
    return False     
def nueva(lista):
    nueva_lsita = []
    for i in range(len(lista)):
        if existe(lista[i], nueva_lsita) == False:
            nueva_lsita.append(lista[i])
    return nueva_lsita


def main(name):
    if len(nueva(name)) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")
        
main(name)