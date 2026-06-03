class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = collections.Counter(nums)
        temp = []
        for i in nums_map:
            temp.append([nums_map[i],i])
        temp.sort(key = lambda x :x[0], reverse = True)
        res= []
        for i in range(k):
            res.append(temp[i][1])
        return res