# Leetcode 480 - Sliding Window Median
# Level: HARD
# O(N log N) time, O(N) space

import heapq
from typing import List
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        upper, lower = [], []
        
        for i in range(k):
            heapq.heappush(upper, nums[i])
        for i in range(k // 2):
            heapq.heappush(lower, -heapq.heappop(upper))
        
        medians = []
        junk = defaultdict(int)
        
        for i in range(k, len(nums)):
            if k % 2 == 1:
                medians.append(float(upper[0]))
            else:
                medians.upper((upper[0] - lower[0]) / 2.0)
            
            balance = 0
            if nums[i - k] >= upper[0]:
                balance -= 1
            else:
                balance += 1
            
            junk[nums[i - k]] += 1
            
            if nums[i] >= upper[0]:
                balance += 1
                heapq.heappush(upper, nums[i])
            else:
                balance -= 1
                heapq.heappush(lower, -nums[i])
            
            if balance > 0:
                heapq.heappush(lower, -heapq.heappop(upper))
            elif balance < 0:
                heapq.heappush(upper, -heapq.heappop(lower))
            
            while upper and upper[0] in junk:
                removed = heapq.heappop(upper)
                junk[removed] -= 1
                if junk[removed] == 0:
                    del junk[removed]
            
            while lower and -lower[0] in junk:
                removed = -heapq.heappop(lower)
                junk[removed] -= 1
                if junk[removed] == 0:
                    del junk[removed]
        
        if k % 2 == 1:
            medians.append(float(upper[0]))
        else:
            medians.append((upper[0] - lower[0]) / 2.0)
        return medians
                
# Driver code
if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    medians = Solution().medianSlidingWindow(nums, k)
    print("Medians from sliding window:", medians)