# Leetcode 295 - Find Median from Data Stream
# Level: HARD
# O(log N) time to addNum, O(1) to findMedian, O(N) space

import heapq

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lower = []
        self.higher = []

    def addNum(self, num: int) -> None:
        if not self.lower or num <= -self.lower[0]:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.higher, num)
        
        if len(self.higher) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.higher))
        elif len(self.lower) > 1 + len(self.higher):
            heapq.heappush(self.higher, -heapq.heappop(self.lower))
        

    def findMedian(self) -> float:
        if len(self.lower) > len(self.higher):
            return float(-self.lower[0])
        return (-self.lower[0] + self.higher[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
