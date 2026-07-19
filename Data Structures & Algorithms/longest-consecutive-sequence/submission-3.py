class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        l=0
        r=1
        count=1
        res=1
        while r<len(nums):
            if nums[l]==nums[r]:
                l=l+1
                r=r+1
            elif nums[r]==nums[l]+1:
                count=count+1
                res=max(count,res)
                l=l+1
                r=r+1
            else:
                count=1
                l=r
                r=r+1
        return res
