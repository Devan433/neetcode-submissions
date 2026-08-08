class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def quick_sort(left, right):
            if left >= right:
                return

            mid = (left + right) // 2

            temp = nums[mid]
            nums[mid] = nums[right]
            nums[right] = temp

            pivot = nums[right]
            i = left

            for j in range(left, right):
                if nums[j] < pivot:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    i += 1

            temp = nums[i]
            nums[i] = nums[right]
            nums[right] = temp

            quick_sort(left, i - 1)
            quick_sort(i + 1, right)

        quick_sort(0, len(nums) - 1)

        return nums