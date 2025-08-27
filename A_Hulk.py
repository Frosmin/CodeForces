n = int(input())

conector = " that "
hate = "I hate"
love  = "I love"
res = "I hate"

if n == 1:
    print(res + " it")
    exit()

res += conector
    



for i in range(n-1):    
    
    if i == n-2:
        if i % 2 == 0:
            res += love + " it"
            print(res)
            exit()
        else:
            res += hate + " it"
            print(res)
            exit()
            
    if i % 2 == 0:
        res += love + conector
    else:
        res += hate + conector
print(res)
