# Leetcode 121 - Best Time to Buy and Sell Stock I
# Level: EASY
# O(N) time, O(1) space

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice= prices[0]
        maxProfit = 0
        for price in prices:
            maxProfit = max(maxProfit, price - minPrice)
            minPrice = min(minPrice, price)
        return maxProfit

# Driver code
if __name__ == '__main__':
    input1 = [7,1,5,3,6,4]
    profit = Solution().maxProfit(input1)
    print("Max profit from input1: ", profit)
    
    input2 = [7,6,4,3,1]
    profit = Solution().maxProfit(input2)
    print("Max profit from input2: ", profit)