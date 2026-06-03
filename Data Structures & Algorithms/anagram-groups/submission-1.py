class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = collections.defaultdict(list)
        for i in strs:
            temp =  [0]*26
            for j in i:
                temp[ord(j)-ord("a")] += 1
            str_map[tuple(temp)].append(i)
        res = []

        for i in str_map:
            res.append(str_map[i])
        return res