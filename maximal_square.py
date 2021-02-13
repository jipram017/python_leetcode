# Leetcode 221 - Maximal Square
# Level: MEDIUM
# O(M*N), O(N) space

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        max_square = 0
        square_sides = [0] * cols
        
        for row in range(rows):
            new_square_sides = [int(matrix[row][0])] + [0 for _ in range(cols - 1)]
            for col in range(1, cols):
                if matrix[row][col] == '1':
                    new_square_sides[col] = 1 + min(new_square_sides[col - 1], square_sides[col], square_sides[col-1])
            max_square = max(max_square, max(new_square_sides))
            square_sides = new_square_sides
        
        return max_square**2

# Driver code 
if __name__ == '__main__':
    input1 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    max_square = Solution().maximalSquare(input1)
    print("Maximal square from input1:", max_square)
        
        