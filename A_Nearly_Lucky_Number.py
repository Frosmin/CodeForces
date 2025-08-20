num  = input()

ciete=num.count('7')
cuatro = num.count('4')

res = ciete+cuatro
if res == 4 or res == 7:
    print("YES") 
else:
    print("NO")


