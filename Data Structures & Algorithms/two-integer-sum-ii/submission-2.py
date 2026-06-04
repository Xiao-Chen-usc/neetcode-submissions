class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left<right:
            sum_lr = numbers[left]+numbers[right]
            if sum_lr == target:
                return [left+1,right+1]
            if sum_lr<target:
                left += 1
                continue
            elif sum_lr>target:
                right -=1
                continue
        