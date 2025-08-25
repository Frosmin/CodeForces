def fibo(n):
    num1 = 0
    num2 = 1
    for _ in range(n):
        print(num2)
        num1,num2 = num2 ,num1+num2
        
    
      



n = int(input())
fibo(n)
 
#1 1
#1 2 
#3 2
# 
# 
# 5 8 13 21