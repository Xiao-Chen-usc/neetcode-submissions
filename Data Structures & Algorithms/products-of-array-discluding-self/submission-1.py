class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix and Suffix
        prefix_product = 1
        prefix_list = []
        suffix_product = 1
        suffix_list = [0]*len(nums)
        for i in nums:
            prefix_list.append(prefix_product)
            prefix_product*=i

        for i in range(len(nums)-1,-1,-1):
            suffix_list[i] = suffix_product
            suffix_product*= nums[i]
        
        res = []
        for i in range(len(nums)):
            res.append(suffix_list[i]*prefix_list[i])
        return res