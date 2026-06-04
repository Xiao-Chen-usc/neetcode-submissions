class Solution:
    def trap(self, height: List[int]) -> int:
        #prefix and suffix
        height_prefix = []
        for i in range(len(height)):
            if i == 0:
                height_prefix.append(height[0])
                continue
            if height[i]>height_prefix[-1]:
                height_prefix.append(height[i])
            else:
                height_prefix.append(height_prefix[-1])
        height_suffix = [0]*len(height)
        for i in range(len(height)-1,-1,-1):
            if i == len(height)-1:
                height_suffix[i] = height[i]
                continue
            if height[i]>height_suffix[i+1]:
                height_suffix[i] = height[i]
            else:
                height_suffix[i] = height_suffix[i+1]
        water = 0
        for i in range(len(height)):
            water += min(height_prefix[i],height_suffix[i])-height[i]
        return water
