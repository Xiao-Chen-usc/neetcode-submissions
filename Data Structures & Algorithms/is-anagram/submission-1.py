class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_1 = collections.Counter(s)
        counter_2 = collections.Counter(t)
        if counter_1==counter_2:
            return True
        else:
            return False