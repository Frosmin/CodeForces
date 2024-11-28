class long:
    def head(word):
        return word[0]
    
    def fin(word):
        return word[-1]

    def resum(num, word):
        if num == 1:
            return long.head(word)
        else:
            return long.fin(word)
            


print(long.resum(1, "word"))