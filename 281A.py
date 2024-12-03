


def main():
    try:
        palabra = input()
        
        
        print(palabra[0].upper() + palabra[1:])
        
    except ValueError as e:
         print(f"Error: {e}")
         
if __name__ == "__main__":
    main()