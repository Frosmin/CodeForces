



for _ in range(int(input())):
    a, b, n = map(int, input().split()) 

    if a == b or n * b <= a:
        print(1)
    else:
        print(2)


# for _ in range(int(input())):
#     a, b, n = map(int, input().split()) 

#     if n * b <= a:
#         print(1)
#     else:
#         print(2)