class Solution:
    def minSwaps(self, s: str) -> int:
        #da finire
        fine=2
        copy=s
        for i in range(len(s)):
            if len(s) == 2 and s[i:fine]== "[]":
                return 0 
            else:
                if s[i:fine] == "[]":
                    copy = copy.replace("[", "",1)
                    copy = copy.replace("]", "",1)
                else:
                    fine+=1
                    if fine == len(s):
                        if copy:
                            
                            return len(copy) //2
                        else:
                            return 0
                   
        
s="]]][[["
sol=Solution()
print(sol.minSwaps(s))