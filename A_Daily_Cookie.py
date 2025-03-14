# def cokies(n, d, s):
#     for j in range(d):
#         if s[j] != '@':
#             return 0
#     return n



# def res (d,s,n):
#     con = 0
#     a = cokies(n,d,s)
#     if a != 0:
#         return a
#     for i in range(d):
#         if s[i] == '.':
#             con += 1
#     return con+(n-d)



# n, d = map(int, input().split())
# s = list(map(str ,input()))

# print(res(d,s,n))

    
def main():
    n,d = input().split()
    s = input()
    count = 0
    for item in s:
        if item == ".":
            count +=1
    count += int(d)
    print(count)
    
if __name__ == "__main__":
    main()




# for i in range(d):
#     s.pop(0)
#     borrados += 1
    
# for i in range (len(s)):
#     if s[i] == '.':
#         print(i+borrados+1)
#         exit()

# print(n) 