
for _ in range(int(input())):
  n, k = map(int, input().split())

  lst = list(map(int, input().split()))
 
  for i in range(min(k, k%2 + 2)):

    mex = 0
    lst = sorted(lst)
    for j in range(n):
      if lst[j] == mex:
        mex += 1

    cnt = [0] * (n + 1)
    for j in range(n):
      cnt[lst[j]] += 1
 
    for j in range(n):
      if lst[j] > mex:
        lst[j] = mex
      else:
        if cnt[lst[j]] > 1:
          lst[j] = mex
    
 
  print(sum(lst))