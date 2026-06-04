class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right = 0,0
        counter = {}
        length = 0 
        while left <= right and right < len(s) and left<len(s):
            if s[right] not in counter:
                counter[s[right] ] = 1
                length = max(length,right-left+1)
                right +=1
                # print(length)
                continue
            if s[right] in counter:
                counter[s[left]] -=1
                if counter[s[left]] == 0:
                    counter.pop(s[left])
                left +=1
        return length
