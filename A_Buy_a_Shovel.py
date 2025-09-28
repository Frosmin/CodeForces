k, r  = map(int, input().split())
plata =0
res = k



for i in range(1,11):
    total=k*i
    if total%10==0 or total%10==r:
        print(i)
        break

# ultimo = k%10

# if ultimo == 5 and r == 5:
#     print(1)
#     exit()

# if ultimo == 5:
#     print(2)
#     exit()

# i = 1

# while (res%10)!= r:
#     res = i*k
#     i+=1

# if i == 1:
#     print(1)
# else:
#     print(i-1)

