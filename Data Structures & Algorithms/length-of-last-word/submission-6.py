class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p=s.split()
        q=len(p)-1
        return len(p[q])
        
        