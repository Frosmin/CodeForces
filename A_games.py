n = int(input())
dic1 = {}
dic2 = {}
res = 0
for _ in range(n):
    a,b = map(int,input().split())
    if a in dic1:
        dic1[a] +=1
    else:
        dic1[a] = 1
    if b in dic2:
        dic2[b] +=1
    else:
        dic2[b] =1
key = 0 
for k, v in dic1.items():
    if k in dic2:
        res += dic2[k]*v
print(res)

    # key value
dic = {1: 10,
       2: 20,
       3: 30}

#para acceder a un valor 
dic[3]   #esto accede a 30
print(dic.get(3))


