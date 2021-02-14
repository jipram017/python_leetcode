# Leetcode 84 - Largest Rectangle in Histogram
# Level: HARD
# O(N) time, O(N) space

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = [0]
        max_area = 0
        
        for i, bar in enumerate(heights):
            while stack and heights[stack[-1]] > bar:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, width * height)
                
            stack.append(i)
            
        return max_area

# Driver code
if __name__ == '__main__':
    input1 = [2,1,5,6,2,3]
    max_area = Solution().largestRectangleArea(input1)
    print("Largest rectangle area from input1: ", max_area)
    
    input2 = [2,4]
    max_area = Solution().largestRectangleArea(input2)
    print("Largest rectangle area from input2: ", max_area)    