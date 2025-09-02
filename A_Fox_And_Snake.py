c,r = map(int,input().split())
bb = True
for i in range(c):
    if i%2 == 0:
        print("#"*r)
    
    else:
        if bb:
            print("."*(r-1) + "#")
            bb = False
        else:
            print("#"+ (r-1)*".")
            bb = True
        