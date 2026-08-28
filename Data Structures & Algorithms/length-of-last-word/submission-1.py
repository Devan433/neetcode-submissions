class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last=len(s)-1
        res=0
        while last>=0 and s[last]==" ":
            last=last-1
        while last>=0:
            if s[last]!=" ":
                res=res+1
                last=last-1
            else:
                break
        return res