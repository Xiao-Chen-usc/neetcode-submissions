class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0 
        right = 0
        count_t = {}
        count_s = {}
        min_length = float("inf")
        res = ""

        for i in range(len(t)):
            count_t[t[i]]=count_t.get(t[i],0)+1
        have = 0
        while left<=right and right<len(s):
            if right == 0:
                count_s[s[right]]=1
                if s[right] in count_t and count_s[s[right]] == count_t[s[right]]:
                    have+=1
            
            if have != len(count_t.keys()):
                right +=1
                if right>=len(s):
                    break
                count_s[s[right]] = count_s.get(s[right],0)+1
                if s[right] in count_t and count_s[s[right]] == count_t[s[right]]:
                    have+=1
            else:
                if right - left +1 < min_length:
                    min_length = right - left +1
                    res = s[left:right+1]
                    print("apple",right,left,s[left:right+1])
                count_s[s[left]] = count_s.get(s[left],0)-1
                if s[left] in count_t and count_s[s[left]] < count_t[s[left]]:
                    have -=1
                left +=1
        return res   

