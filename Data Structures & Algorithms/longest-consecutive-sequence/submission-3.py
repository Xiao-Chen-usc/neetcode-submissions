class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_res = 0 
        for i in nums:
            res = []
            res.append(i)
            if i-1 not in nums_set:
                cur = i
                while True:
                    if cur+1 in nums_set:
                        cur += 1
                        res.append(cur)
                    else:
                        break
            max_res = max(max_res,len(res))
        return max_res
                