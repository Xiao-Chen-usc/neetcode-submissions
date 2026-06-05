from typing import List
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))
        ans = []
        ans.append(-heap[0][0])
        for i in range(k,len(nums)):
            heapq.heappush(heap,(-nums[i],i))
            while i-k+1 >heap[0][1]:
                heapq.heappop(heap)
            ans.append(-heap[0][0])
        return ans
            