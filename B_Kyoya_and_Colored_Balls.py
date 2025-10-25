
res=1
s=0

for _ in range(int(input())):
	n=int(input())
	s+=n
	if s==n:continue
	k=1
	for i in range(1,n):
		k=k*(s-i)//i
	res=(res*k)%(10**9+7)
print(res)

