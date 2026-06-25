class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        count=0
        res=set()
        for email in emails:
            out=""           
            local,domain=email.split("@")
            local=local.split("+")[0]
            local=local.replace(".","")
            out=local+"@"+domain
            res.add(out)        
            
        return len(res)
