# Leetcode 122 - Best Time to Buy and Sell Stock II
# Level: EASY
# O(N) time, O(N) space

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([max(0, prices[i]-prices[i-1]) for i in range(1, len(prices))])

# Driver code
if __name__ == '__main__':
    input1 = [7,1,5,3,6,4]
    profit = Solution().maxProfit(input1)
    print("Maximum profit from input1: ", profit)
    
    input2 = [1,2,3,4,5]
    profit = Solution().maxProfit(input2)
    print("Maximum profit from input2: ", profit)