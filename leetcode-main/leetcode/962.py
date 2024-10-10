class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        massimo=0
        inizio =0
        fine =len(nums)-1
        while inizio != len(nums)-1:
            if inizio < fine and nums[inizio]<=nums[fine]:
                    temp=fine-inizio
                    if massimo < temp:
                        massimo = temp
            fine-=1
            if fine == inizio:
                fine=len(nums)-1
                inizio +=1
        return massimo
            
n=[6,0,8,2,1,5]
sol=Solution()
print(sol.maxWidthRamp(n))

"""class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        massimo=0
        n=len(nums)
        for i,v in enumerate(nums):
            for j in range(n-1, -1, -1):
                if i < j and v<=nums[j]:
                    temp=j-i
                    if massimo < temp:
                        massimo = temp
        return massimo"""