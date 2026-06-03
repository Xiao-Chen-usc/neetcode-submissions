class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
           res += str(len(i)) + "#"
           res+=i
        return res

    def decode(self, s: str) -> List[str]:
        print("decode")
        num = 0
        i = 0
        ans = []
        while i < len(s):
            if s[i].isdigit():
                num*=10
                num+=int(s[i])
                i+=1
            elif s[i]=="#":
                ans.append(s[i+1:i+num+1])
                i+=num+1
                num = 0
        return ans
                
