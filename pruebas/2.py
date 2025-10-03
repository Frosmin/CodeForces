n = 5

a= [1,2,3,4,5,0,0] #cuenta repeticiones de numeros
hash=[0]*(n+1)
for item in a:
   hash[item]+=1

print(hash)