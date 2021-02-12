# Leetcode 123 - Best Time to Buy and Sell Stock III
# Level: HARD
# O(N) time, O(N) space

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_price, max_profit = prices[0], prices[len(prices) - 1], 0
        
        left = [0] * len(prices)
        for i in range(1, len(prices), 1):
            min_price = min(min_price, prices[i])
            left[i] = (max(left[i-1], prices[i] - min_price))
        
        right = [0] * len(prices)
        for i in range(len(prices)-2, -1, -1):
            max_price = max(max_price, prices[i])
            right[i] = (max(right[i+1], max_price - prices[i]))
        
        for i in range(len(prices)):
            max_profit = max(max_profit, left[i] + right[i])
        return max_profit

# Driver code
if __name__ == '__main__':
    input1 = [1,2,3,4,5]
    max_profit = Solution().maxProfit(input1)
    print("Max profit from input1 is:", max_profit)
    
    input2 = [3,3,5,0,0,3,1,4]
    max_profit = Solution().maxProfit(input2)
    print("Max profit from input2 is:", max_profit)
    
    input3 = [7,6,4,3,1]
    max_profit = Solution().maxProfit(input3)
    print("Max profit from input3 is:", max_profit)      
    
    input4 = [1]
    max_profit = Solution().maxProfit(input4)
    print("Max profit from input4 is:", max_profit)          