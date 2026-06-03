class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_sort = [[] for _ in range(len(nums)+1)]
        counter = collections.Counter(nums)
        reversed_counter = []
        for i in counter:
            bucket_sort[counter[i]].append(i)
        ans = []
        for i in range(len(bucket_sort)-1,-1,-1):
            if bucket_sort[i]:
                ans+=bucket_sort[i]
                if len(ans) == k:
                    return ans
        return ans
