class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        i=0
        res=[]
        for i in range(n):
            if nums[i]!=1:
                count=0
                res.append(count)
            else:
                count=count+1
                res.append(count)            
        return(max(res))