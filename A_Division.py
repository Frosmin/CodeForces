n = int(input())
for _ in range(n):
    num = int(input())
    if num <= 1399:
        div= 4
    elif num >= 1400 and num <=1599:
        div = 3
    elif num >=1600 and num <=1899:
         div = 2
    elif num >=1900:
        div = 1
    
    
    
    print(f"Division {div}" )