# Leetcode 1559 - Detect Cycle in 2D Graph
# Level: HARD
# O(M*N) time, O(M*N) space

from typing import List

class Solution:
    def __init__(self):
        self.hasCycle = False
        
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        
        # Initialize parent array
        parent = [i for i in range(rows * cols)]
        
        for i in range(rows):
            if self.hasCycle:
                return True
            for j in range(cols):
                if self.hasCycle:
                    return True
                
                val = i * cols + j
                if j != cols - 1 and grid[i][j] == grid[i][j + 1]:
                    self.union_find(parent, val, val + 1)
                if i != rows - 1 and grid[i][j] == grid[i + 1][j]:
                    self.union_find(parent, val, val + cols)
        
        return self.hasCycle
    
    def union_find(self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        if x_set == y_set:
            self.hasCycle = True
        parent[x_set] = y_set
    
    def find_parent(self, parent, m):
        if parent[m] == m:
            return m 
        if parent[m] != m:
            return self.find_parent(parent, parent[m])

# Driver code
if __name__ == '__main__':
    grid1 = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
    grid2 = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
    grid3 = [["a","b","b"],["b","z","b"],["b","b","a"]]
    hasCycle = Solution().containsCycle(grid2)
    if hasCycle:
        print("Grid 2 contains cycle")
    else:
        print("Grid 2 is free of cycle")