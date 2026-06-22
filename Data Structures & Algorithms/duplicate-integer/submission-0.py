class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new=[]
        new=set(nums)
        count1=len(nums)
        count2=len(new)
        if count2<count1:
            return True
        else:
            return False