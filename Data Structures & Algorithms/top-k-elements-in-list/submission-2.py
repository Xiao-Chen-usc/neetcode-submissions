class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort
        nums_freq = [[] for _ in range(len(nums)+1)]
        nums_map = {}
        res = []
        for i in nums:
            nums_map[i] = nums_map.get(i,0)+1
        for i in nums_map:
            nums_freq[nums_map[i]].append(i)
        for i in range(len(nums_freq)-1,0,-1):
            if not nums_freq[i]:
                continue
            for j in nums_freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return res
