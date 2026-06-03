class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # HashSet（集合查找）+ Sequence Start Expansion
#         Set 存所有值
# 只从合法起点开始
# while 往后扩展
# 更新最长/数量/结果
        max_num = 0
        nums_set = set(nums)
        for i in range(len(nums)):
            if nums[i] -1 not in nums_set:
                res = set()
                res.add(nums[i])
                cur= nums[i]
                while True:
                    if cur +1 in nums_set:
                        res.add(cur +1)
                        cur += 1
                    else:
                        break
                max_num = max(max_num,len(res))
            
        return max_num