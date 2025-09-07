n = int(input())
# for _ in range(n):
#     num = int(input())
#     if len(lst) < num:
#         while len(lst) != num:
#             if i % 3 != 0 and i%10 != 3:
#                     lst.append(i)
#                     i+=1
#             else:
#                 i+=1
#     else:
#         print(lst[num])                  
#     print(lst[num-1])

for _ in range(n):
    num = int(input())
    i = 0
    res = 0
    while i < num:
        res+=1
        if res % 3 == 0 or res%10 == 3:
            continue
        i +=1              
    print(res)
            