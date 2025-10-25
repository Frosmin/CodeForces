

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n=int(input())
a=list(map(int,input().split()[:n]))
ret=0
v=a[0]
for i in range(1,n):
    v=gcd(v,a[i])
if(v!=1):
    print("YES\n"+str(0))
    exit()
for i in range(n):
    if(a[i]%2==0):
        continue
    elif(i+1==n):
        ret+=2
    else:
        if(a[i+1]%2==0):
            ret+=2
        else:
            ret+=1
            a[i+1]=2
print("YES\n"+str(ret))