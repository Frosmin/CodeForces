# word = list(map(str, input()))
# if len(word) <= 5:
#     print("NO")
#     exit()
    
# h = word.count("h")
# e = word.count("e")
# l = word.count("l")
# o = word.count("o")
# print("YES" if h >= 1 and e >= 1 and l >= 2 and o >= 1 else "NO")

# w = "hello"
# word = list(map(str, input()))
# j = 0
# res = 0
# #print(len(word))
# for i in range(len(word)):
    
#     if word[i] == w[j]:
#         res += 1
#         j += 1
#         if res == 5:
#             print("YES")
#             exit()
# print("NO")

w = "hello"
s = input()
j = 0
for c in s:
    if c == w[j]:
        j += 1
        if j == len(w):
            print("YES")
            break
else:
    print("NO")