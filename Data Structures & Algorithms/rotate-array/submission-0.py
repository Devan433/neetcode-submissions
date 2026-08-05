class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        l=0
        r=len(nums)-1
        def rever(l,r):
            while l<r:
                temp=nums[l]
                nums[l]=nums[r]
                nums[r]=temp
                l=l+1
                r=r-1
        rever(0,len(nums)-1)
        rever(0,k-1)
        rever(k,len(nums)-1)






