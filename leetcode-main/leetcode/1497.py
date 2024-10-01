class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        index=0
        index1=1 #parti da sotto
        while  index != len(arr):
            var = arr[index]
            var1 = arr[index1]
            somma=var+var1
            if somma % k == 0:
                arr.remove(var)
                arr.remove(var1)
                index1-=1
            else:
                if index1 != len(arr)-1:
                    index1+=1
                else:
                    index+=1
                    index1=1
                if index == len(arr):
                    if arr:
                        return False
                    else:
                        return True
            
                    
arr = [1,2,3,4,5,10,6,7,8,9]
k = 5
sol=Solution()
print(sol.canArrange(arr, k))
                        
                
            