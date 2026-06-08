class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag={}
        for word in strs:
            signature ="".join(sorted(word))
            if signature in anag:
                anag[signature].append(word)
            else:
                anag[signature]=[word]
        return list(anag.values())