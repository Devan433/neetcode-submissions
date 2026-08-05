class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        l=0
        r=len(heights)-1
        while l<r:
            total=(r-l)*min(heights[l],heights[r])
            res=max(total,res)
            if heights[l]>heights[r]:
                r=r-1
            else:
                l=l+1
        return res
      