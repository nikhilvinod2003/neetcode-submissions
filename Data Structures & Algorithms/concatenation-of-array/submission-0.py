class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        i=0
        for i in range(n):
            ans.append(nums[i])
        for i in range(n):
            ans.append(nums[i])
        return ans