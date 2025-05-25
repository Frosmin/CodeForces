
class Solution(object):
    def isPalindrome(self, x):
        list = [int(digit) for digit in str(x)]
        for i in range(len(list)//2):
            if list[i] != list[-(i+1)]:
                return False
        return True
