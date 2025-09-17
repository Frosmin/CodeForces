a = int(input())
b = int(input())
c = int(input())
lst = []
lst.append((a+b)*c)
lst.append(a*(b+c))
# lst.append((a+c)*b)
lst.append(a*b*c)
lst.append(a+b+c)
print(max(lst))

