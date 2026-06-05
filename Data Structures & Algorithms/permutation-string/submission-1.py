class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = {}
        counter_s2 = {}
        if len(s1)>len(s2):
            return False
        for i in range(len(s1)):
            counter_s1[s1[i]] = counter_s1.get(s1[i],0)+1
            counter_s2[s2[i]] = counter_s2.get(s2[i],0)+1
        if counter_s2 == counter_s1:
            return True
        for i in range(len(s1),len(s2),1):
            counter_s2[s2[i]] = counter_s2.get(s2[i],0)+1
            counter_s2[s2[i-len(s1)]] = counter_s2[s2[i-len(s1)]]-1
            # print(counter_s2,s2[i-len(s1)],i-len(s1))
            if counter_s2[s2[i-len(s1)]] == 0:
                counter_s2.pop(s2[i-len(s1)])
            if counter_s2 == counter_s1:
                return True
        return False