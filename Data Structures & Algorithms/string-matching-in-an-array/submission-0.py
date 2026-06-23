class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        for word in words:
            count=0
            for i in range(len(words)):
                if word in words[i]:
                    count+=1
            if count>1:
                res.append(word)
        return res
