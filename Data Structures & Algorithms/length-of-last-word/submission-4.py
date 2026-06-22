class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1=s.strip(" ")
        if len(s1)==0:
            return 0
        if len(s1)==1:
            return 1
        print(s1)
        i=-1
        k=""
        while(s1[i]!=" "):
            k+=s[i]
            i-=1

        return len(k)

