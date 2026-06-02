class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_1 = {}
        counter_2 = {}
        for i in s:
            counter_1[i] = counter_1.get(i,0) + 1
        for i in t:
            counter_2[i] = counter_2.get(i,0) + 1
        if counter_1==counter_2:
            return True
        else:
            return False