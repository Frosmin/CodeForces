
def aprobados(n, k, scores):
    res = 0
    
    for i in range(0, n):
        if aproved(scores[i],k):
            res +=1
        else:
            pass
    return res

def aproved(num,k):
    if num>k:
        return True
    else:
        return False









def main():
    try:
        n, k = map(int, input().strip().split())
        
        if not (1 <= k <= n <= 50):
            raise ValueError("error")
        
        scores = list(map(int, input().strip().split()))
        print(aprobados(n, k, scores))
        
    except ValueError as e:
        print(f"Error: {e}")
    
    
if __name__ == "__main__":
    main()