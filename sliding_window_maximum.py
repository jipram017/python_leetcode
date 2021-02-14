# Leetcode 239 - Sliding Window Maximum
# Level: HARD
# O(N) time, O(N) space

from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        max_window = []
        
        for i, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(i)
            
            if q[0] <= i - k:
                q.popleft()
            if i >= k - 1:
                max_window.append(nums[q[0]])
                
        return max_window
                
# Driver code
if __name__ == '__main__':
    input1 = [1,3,-1,-3,5,3,6,7]
    k = 3
    max_window = Solution().maxSlidingWindow(input1, k)
    print("Maximal sliding window from input1:", max_window)