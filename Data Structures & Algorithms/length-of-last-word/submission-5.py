class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p=s.split()
        n=len(p[-1])
        return n