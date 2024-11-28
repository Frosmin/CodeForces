def aprobados(n, nota, scores):
    res = 0
    for i in range(0, n):
        
        
        if aproved(scores[i],nota):
            res +=1
        else:
            pass
    return res
    
    
def aproved(num,k):
    if num >= k and num > 0:
        return True
    else:
        return False




def main():
    try:
        n, k = map(int, input().strip().split())
        
        if not (1 <= k <= n <= 50):
            raise ValueError("error")
        
        scores = list(map(int, input().strip().split()))
        
        nota = scores[k-1]
        
        print(aprobados(n, nota, scores))
        
    except ValueError as e:
        print(f"Error: {e}")
    
    
if __name__ == "__main__":
    main()