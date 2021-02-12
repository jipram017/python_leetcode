# Leetcode 765 - Couple Holding Hands
# Level: HARD
# O(N) time, O(N) space

from typing import List

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        parent = [0]*len(row)
        for r in row:
            parent[r] = 2 * (r // 2)
        
        maxConnectedComponents = len(row) // 2
        curConnectedComponents = maxConnectedComponents
        
        for i in range(0, len(row), 2):
            g1 = self.find_parent(parent, row[i])
            g2 = self.find_parent(parent, row[i+1])
            if g1 != g2:
                parent[g1] = g2
                curConnectedComponents -= 1
        
        return maxConnectedComponents - curConnectedComponents
    
    def find_parent(self, parent, m):
        if parent[m] == m:
            return m 
        elif parent[m] != m:
            return self.find_parent(parent, parent[m])

# Driver code
if __name__ == '__main__':
    row1 = [0, 2, 1, 3]
    min_swaps = Solution().minSwapsCouples(row1)
    print("Minimum swaps needed from row1:", min_swaps)
    
    row2 = [3, 2, 0, 1]
    min_swaps = Solution().minSwapsCouples(row2)
    print("Minimum swaps needed from row2:", min_swaps)
                
        
            

