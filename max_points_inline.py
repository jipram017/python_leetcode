# Leetcode 149 - Maximum Points in A Line
# Level: HARD
# O(N**2) time, O(N) space

from collections import defaultdict
from decimal import Decimal
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
         
        overall_max = 2
         
        for i, point_1 in enumerate(points):
            gradients = defaultdict(int)
            max_points = 1
            
            for point_2 in points[i + 1:]:
                if point_2[0] == point_1[0]:
                    if point_2[1] == point_1[1]:
                        max_points += 1         # Handle duplicate points
                    else:
                        gradients['inf'] += 1   # Handle vertical lines
                else:
                    gradient = Decimal (point_2[1]-point_1[1]) / Decimal (point_2[0]-point_1[0])
                    gradients[gradient] += 1
                    
            if gradients:
                max_points += max(gradients.values())
            overall_max = max(overall_max, max_points)
            
        return overall_max

# Driver code
if __name__ == '__main__':
    input1 =  [[1,1],[2,2],[3,3]]
    maxpoints = Solution().maxPoints(input1)
    print("Max points in line for input1 is ", maxpoints)
    
    input2 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    maxpoints = Solution().maxPoints(input2)
    print("Max points in line for input2 is ", maxpoints)