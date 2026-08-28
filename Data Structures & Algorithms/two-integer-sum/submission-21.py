class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        items={}
        for i ,num in enumerate(numbers):
            difference=target-num
            if difference in items:
                return [items[difference],i]
            else:
                items[num]=i
        return []