
# def twoSum(nums: list[int], target: int) -> list[int] | None:
        
#         for i in range(len(nums)):
#                 for j in range(i + 1, len(nums)):      
#                         somma: int = nums[i] + nums[j]
                        
#                         if somma == target:
                                
#                                 return [i, j]
                        
#         return None
# num = [2,7,11,15]
# targe = 9
# print(twoSum(num,targe))


def twoSum(nums: list[int], target: int) -> list[int]:
        result = [(i,y) for i in range(len(nums)) for y in range(i+1 , len(nums)) if nums[i]+nums[y]==target]
        if result:
                return result
        # for i in range(len(nums)):
        #         for j in range(i + 1, len(nums)):      
        #                 somma: int = nums[i] + nums[j]
                        
        #                 if somma == target:
                                
        #                         return [i, j]
        
num = [2,7,11,15]
targe = 9
print(twoSum(num,targe))