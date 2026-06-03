class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s)-1
        while left<right:
            # print(left,right)
            if not s[left].isalnum():
                left +=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            if s[right].lower() == s[left].lower():
                left +=1
                right -=1
            else:
                # print("final",left,right)
                return False
        return True