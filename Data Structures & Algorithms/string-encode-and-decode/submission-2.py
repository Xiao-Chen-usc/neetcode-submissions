class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res+=str(len(i))
            res+="#"
            res+=i
        return res
        #    4#luck3#yes


    def decode(self, s: str) -> List[str]:
        res = []
        cur = 0
        length = 0
        while True:
            if cur >= len(s):
                break
            if s[cur].isdigit():
                length = length*10 + int(s[cur])
                cur += 1
            elif s[cur] == "#":
                word = s[cur+1:cur+1+length]
                cur = cur+1+length
                res.append(word)
                length = 0
            
        return res


