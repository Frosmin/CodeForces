for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    cruces = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] >= a[j]:
                cruces += 1
    
    print(cruces)





 
 
def merge(array, left, right):
 
    if(right > left):
        medio = (right + left) //2
        temp1 = array[left:medio+1]
        temp2 = array[medio+1:right +1]
 

        
        temp1.append(10**6)
        temp2.append(10**6)
        j = 0
        k = 0
        contador = 0
 
        for i in range(left, right + 1):
            if(temp2[k] <= temp1[j]):
                array[i] = temp2[k]
                if(temp1[j] != 10**6):
                    contador = contador + (medio - left - j) + 1
                k = k + 1
 
            else:
                array[i] = temp1[j]
                j = j + 1
 
        return contador
 
 
    else:
        return 0
    
 
def merge_sorte(array, left, right):
    if(right > left):
        medio = (right + left) //2
        izq = merge_sorte(array, left, medio)
        der = merge_sorte(array, medio +1, right)
        merge_c = merge(array, left, right)
 
 
        return izq + der + merge_c
 
    else:
        return 0
    
 
 

 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(merge_sorte(a, 0, n-1))