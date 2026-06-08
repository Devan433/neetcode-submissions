class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map={}
        for n in nums:
            if n in count_map:
                count_map[n]+=1
            else:
                count_map[n]=1
        pairs=list(count_map.items())
        pairs.sort(key=lambda x:x[1],reverse=True)
        res=[]
        for i in range(k):
            res.append(pairs[i][0])
        return res
        