
def indentificardoOperacion(word):
    if word == "++X" or word == "X++":
        return 1
    elif word == "--X" or word == "X--":
        return -1



def main():
    try:
        
        n = int(input().strip())
        
        if not 1 <= n <= 150:
            raise ValueError("El número de palabras debe estar entre 1 y 100")
            
        res = 0
        for _ in range(n):
            word = input().strip()
            res += indentificardoOperacion(word)
        print(res)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()