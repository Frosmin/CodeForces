def sruma_votos(votos):
    suma = int(votos[0]) + int(votos[2]) + int(votos[4])
    return suma
    
    
    


def main():
    try:
        n = int(input().strip())
        if not 1 <= n <= 1000:
            raise ValueError("error")
        
        res = 0
        
        for _ in range(n):
            votos = input().strip()
            if sruma_votos(votos) >= 2:
                res += 1
        print(res)
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()