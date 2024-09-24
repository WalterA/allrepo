class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        arr1= list(map(str, arr1))
        for i in arr1:
        arr2=list(map(str,arr2))
        lista=[]
        conta=0
        for str1, str2 in zip(arr1, arr2):
            conta = 0
            for c1, c2 in zip(str1, str2):
                if c1 == c2:
                    conta += 1
                
            lista.append(conta)
        return sum(lista)
            
            
arr1 = [1,10,100]
arr2 = [1000]
sol=Solution()
print(sol.longestCommonPrefix(arr1,arr2))
            
        