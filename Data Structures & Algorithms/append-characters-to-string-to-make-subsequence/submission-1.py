class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s1=list(s)
        t1=list(t)
        count=0
        i=0
        for word in t:
            while len(s1)>=1:
                if s1[i]==word:
                    count+=1
                    s1.pop(0)
                    break
                else:
                    s1.pop(0)                     
        return len(t)-count 