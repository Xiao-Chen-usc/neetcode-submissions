class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_prefix = []
        high_suffix = [-float("inf")]*len(prices)
        lowest = float("inf")
        for i in range(len(prices)):
            if prices[i]<lowest:
                lowest = prices[i] 
            lowest_prefix.append(lowest)
        highest = -float("inf")
        for i in range(len(prices)-1,-1,-1):
            if prices[i]>highest:
                highest = prices[i]
            high_suffix[i] = highest
        highest_profit = 0
        for i in range(len(prices)):
            # print(high_suffix)
            # print(lowest_prefix)
            highest_profit = max(highest_profit,high_suffix[i]-lowest_prefix[i])
        return highest_profit
