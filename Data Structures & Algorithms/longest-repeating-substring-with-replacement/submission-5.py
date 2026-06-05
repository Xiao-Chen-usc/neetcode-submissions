class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right = 0,0
        count = {}
        max_freq = 0
        max_length = 0
        while left<=right and right<len(s):
            count[s[right]] = count.get(s[right],0) + 1
            length = right - left+1
            #length - max_freq <= k
            #length<=k+max_freq max_length = k + max_freq
            max_freq = max(count[s[right]],max_freq)
            if length - max_freq > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    count.pop(s[left])
                left+=1
            max_length = max(max_length,right-left+1)
            right +=1
        return max_length
            
            
