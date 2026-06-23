class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out={}
        for word in strs:
            key="".join(sorted(word))
            if key not in out:
                out[key]=[]
            out[key].append(word)
        return list(out.values())
            