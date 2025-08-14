class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        lista_nueva = num1 + num2
        lista_nueva.sort()
        tam = len(lista_nueva)
        if tam % 2 == 0:
            mitad= (tam // 2)-1
            print((lista_nueva[mitad]+lista_nueva[mitad+1]/2 ))
        else:
            mitad = (tam//2)
            print(lista_nueva[mitad])
            
            
        
    
    
    
num1 = [1,3]
num2 = [2]
solu = Solution()
solu.findMedianSortedArrays(num1, num2)

