class long:
    def head(word):
        return word[0]
    
    def fin(word):
        return word[-1]
    
    def tam(word):
     return len(word)

    def resum(num, word):
        if num == len(word):
            return word
        elif num == 1:
            return long.head(word)
        else:
            return long.head(word) + str(len(word)-2) + long.fin(word)
 
print(long.resum(4, "localization"))