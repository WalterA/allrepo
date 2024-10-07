from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        *Memory Limit Exceeded
        massimo = []
        index=0
        def ric(nums, k,massimo,index ):
            gruppo = nums[index:k]
            massimo.append(max(gruppo))
            index+=1
            k+=1
            if k > len(nums):
                return massimo
            else:
                return ric(nums,k,massimo,index)
        return ric(nums, k,massimo,index )
        
        #Memory Limit Exceeded
        massimo = []
        for i in range(len(nums)):
            massimo.append(max(nums[i:k]))
            if k == len(nums):
                return massimo
            else:
                k+=1
        return massimo
        """

        gruppo = []
        maxy = []

        for i in range(len(nums), k):
            maxy.append(max(nums[i:k]))
            k+1
        return maxy


# Esempio di utilizzo
nums=[1,3,-1,-3,5,3,6,7]
k=3
sol=Solution()
print(sol.maxSlidingWindow(nums,k))
            
