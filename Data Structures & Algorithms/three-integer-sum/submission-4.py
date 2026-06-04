class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        nums.sort()
        for i in range(len(nums)):
            left = i+1
            right = len(nums) -1
            while left <right:
                sum_3 = nums[i]+nums[left]+nums[right]
                if sum_3 > 0:
                    right -=1
                elif sum_3 < 0:
                    left += 1
                else:
                    if (nums[i],nums[left],nums[right]) not in visited:
                        res.append([nums[i],nums[left],nums[right]])
                        visited.add((nums[i],nums[left],nums[right]))
                    right -=1
                    left += 1
                    continue
                    
        return res
