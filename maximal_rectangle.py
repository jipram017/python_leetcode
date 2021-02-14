# Leetcode 85 - Maximal Rectangle
# Level: HARD
# O(M*N) time, O(N) space

from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        max_rectangle = 0
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * (cols + 1)
        
        for row in range(rows):
            heights = [heights[col] + 1 if matrix[row][col] == '1' else 0 for col in range(cols)] + [0]
            stack = [0]
            
            for col in range(1, len(heights)):
                while stack and heights[stack[-1]] > heights[col]:
                    height = heights[stack.pop()]
                    if stack:
                        width = col - stack[-1] - 1
                    else:
                        width = col
                    max_rectangle = max(max_rectangle, width * height)
                    
                stack.append(col)
        
        return max_rectangle
            
# Driver code
if __name__ == '__main__':
    input1 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    max_rectangle = Solution().maximalRectangle(input1)
    print("Maximal rectangle from input1: ", max_rectangle)