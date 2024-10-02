class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        #METTERE LISTA DI RANGE DI LEN(ARR)
        copy=arr.copy()
        copy=sorted(copy)
        copy=list(set(copy))
        if len(set(arr))==1:
            lista=[1]*len(arr)
            return lista
        for i in range(len(copy)):
            while copy[i] in arr:
                arr[arr.index(copy[i])]=i+1
       
        return arr
        
    

arr = [37,12,28,9,100,56,80,5,12]
print(arr)
copy=arr.copy()
copy=sorted(copy)
print(copy)
sol = Solution()
print(sol.arrayRankTransform(arr))