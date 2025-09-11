lst  = list(map(str, input()))
i = 0 
while i < len(lst):
    if lst[i] == "-" and lst[i+1] == "-":
        print(2,end="")
        i+=2
    elif lst[i] == "-" and lst[i+1] == ".":
        print(1,end="")
        i+=2
    else:
        print(0,end="")
        i+=1

