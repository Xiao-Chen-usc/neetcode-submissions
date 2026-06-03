class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strs_dict = collections.defaultdict(list)
        res = []
        for i in strs:
            map = [0]*26
            for j in i:
                map[ord(j)-ord("a")] +=1
            strs_dict[tuple(map)].append(i)
        for i in strs_dict:
            res.append(strs_dict[i])
        return res
