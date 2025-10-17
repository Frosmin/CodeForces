
for _ in range(int(input())):
  n=int(input())
  if n == 36:
    print("YES")
    print(5,6,10,15)
  elif n == 40:
    print("YES")
    print(5,6,14,15)
  elif n == 44:
    print("YES")
    print(6,7,10,21)
  elif n >= 31:
    print("YES")
    print(6,10,14,n-30)
  else:
    print("NO")