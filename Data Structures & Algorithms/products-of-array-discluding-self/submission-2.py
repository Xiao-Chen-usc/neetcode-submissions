class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = []
        suffix_product = [0]*len(nums)
        product = 1
        for i in range(len(nums)):
            prefix_product.append(product)
            product *= nums[i]
        product = 1
        for i in range(len(nums)-1,-1,-1):
            suffix_product[i] = product
            product *= nums[i]
        res = []
        for i in range(len(nums)):
            res.append(prefix_product[i]*suffix_product[i])
        return res

