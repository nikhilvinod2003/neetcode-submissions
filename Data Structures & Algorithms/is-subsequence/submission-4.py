class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1=list(s)
        t1=list(t)
        count=0
        i=0
        for word in s:
            while len(t1)>=1:
                if t1[i]==word:
                    count+=1
                    t1.pop(0)
                    break
                else:
                    t1.pop(0)
        print(count)
        if count==len(s):
            return True
        else:
            return False 
        