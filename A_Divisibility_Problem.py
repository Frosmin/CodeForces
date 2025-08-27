import sys
input = sys.stdin.readline


def multiplo(a,b):
    res = 0
    i = 1
    while res < a:
        res = b*i
        i += 1
    return res
        

n =int(input())

for _ in range(n):
    a,b = map(int,input().split())
    if a%b!=0:
        print(multiplo(a,b)-a)
    else:
        print(0)
    
    
    
    
    


n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    
    if a%b!=0:
        print( ((a//b)+1)*b-a )
    else:
        print(0)