class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        temp={}
        if len(set(s))==len(set(t))==len(set(zip(s,t))):
            return True
        return False
        