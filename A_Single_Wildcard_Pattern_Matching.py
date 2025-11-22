# a, b = map(int, input().split())
# s1 = input()
# s2 = input()
 
# if (s1.find("*")>=0):
#     m = s1.split('*')
   
#     s2=s2.removeprefix(m[0]).removesuffix(m[1])
#     if(len(s2)==b-len(m[0])-len(m[1])):
#         print("YES")
#     else:
#         print("NO")
# else:
#     if (s1==s2):
#         print("YES")
#     else:
#         print("NO")




# n, m = map(int,input().split())
# s = input()
# t = input()
# if len(t)>=len(s)-1:
#     if '*' in s:
#         s = s.split('*')
#         if not len(s[0])+len(s[1]):
#             print('YES')
#             exit()
#         if not len(s[0]):
#             if t[-len(s[1]):] == s[1]:
#                 print('YES')
#                 exit()
#             else:
#                 print('NO')
#                 exit()
#         if not len(s[1]):
#             if t[:len(s[0])] == s[0]:
#                 print('YES')
#                 exit()
#             else:
#                 print('NO')
#                 exit()
#         if t[:len(s[0])] == s[0]:
#             if t[-len(s[1]):] == s[1]:
#                 print('YES')
#                 exit()
#         print('NO')
#         exit()  
#     else:
#         if s == t:
#             print('YES')
#         else:
#             print('NO')
# else:
#     print('NO')

n, m = map(int, input().split())
s = input()
ta = input()

if '*' in s:
    pre, suf = s.split('*')
    if len(ta) >= len(pre) + len(suf) and ta.startswith(pre) and ta.endswith(suf):
        print('YES')
    else:
        print('NO')
else:
    print('YES' if s == ta else 'NO')