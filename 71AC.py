
def resum(word):
        if len(word) <= 10:
            return word
        else:
            return f"{word[0]}{len(word)-2}{word[-1]}"


def main():
    try:
        
        n = int(input().strip())
        
        
        if not 1 <= n <= 100:
            raise ValueError("El número de palabras debe estar entre 1 y 100")
            
    
        for _ in range(n):
            word = input().strip()
            print(resum(word))
            
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    
    
    
    
