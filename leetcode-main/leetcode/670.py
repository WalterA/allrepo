class Solution:
    def maximumSwap(self, num: int) -> int:
        temp=0
        stinga= str(num)
        temp=int(stinga[0])
        for i in stinga:
            if temp>int(stinga[0]):
                stinga[0]=str(temp)
                break
            else:
                temp=int(i)
        return int(stinga)

s=Solution()
print(s.maximumSwap(2736)) # 7236
                
    
            