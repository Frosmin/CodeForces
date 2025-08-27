# def repeticion (x,y):
#     prod = 0
#     while y!=0:
#         prod += x
#         y -=1
#     return prod

# print(repeticion(5,2))

# def fromu(a,b):
#    return ((a//b)+1)*b-a
# a= 123
# b = 456
# print(123%456)
# print(fromu(a,b))



a = set("HQ9S")       # {'H','Q','9'}
b = set("SAMUEL")    # {'S','A','M','U','E','L'}

print(bool(a & b))         # intersección: conjunto de caracteres comunes -> set() o {'A'} si A está en ambos
print("H" in a)      # True