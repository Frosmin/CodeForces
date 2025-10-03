for _ in range(int(input())):
   n,k=map(int,input().split())
   a=list(map(int,input().split()))
   hash=[0]*(n+1)
   for i in a:
      hash[i]+=1
   bb=True
   for i in range(1,n+1):
      if hash[i]%k!=0:
         bb=False
      else:
         hash[i]//=k
   if bb==False:
      print(0)
   else:
      res=0
      count=[0]*(n+1)
      l=0
      r=0
      while r<n:
         count[a[r]]+=1
         while count[a[r]]>hash[a[r]]:
            count[a[l]]-=1
            l+=1
         res+=r-l+1
         r+=1
      print(res)