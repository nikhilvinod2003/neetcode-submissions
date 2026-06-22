class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            s1="".join(sorted(s))
            t1="".join(sorted(t))
            n=len(t1)
            for i in range(n):
                if s1[i]!=t1[i]:
                    return False
            return True
        else:
            return False