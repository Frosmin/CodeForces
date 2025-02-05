

n, k = input().split()



def subtraction(n,k):
    for i in range (int(k)): 
        if (int(n)%10 == 0):
            n = int(n)//10
        else:
            n = int(n) - 1
    return n

res = subtraction(n,k)
print (res)
