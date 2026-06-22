class Solution:
    def countSeniors(self, details: List[str]) -> int:
        n=len(details)
        count=0
        s=" "
        for num in details:
            s+=num[11]
            s+=num[12]
            s+=" "
        age = list(map(int, s.split()))
        for i in age:
            if i>60:
                count+=1
        return count