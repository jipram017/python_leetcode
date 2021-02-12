# Leetcode 1161 - Maximum Level Sum of a Binary Tree
# Level: MEDIUM
# O(N) time, O(N) space

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = []
        level, result, max_sum = 1, 1, float('-inf')
        queue.append(root)
        
        while queue:
            qSize, cSum = len(queue), 0
            for i in range(qSize):
                node = queue.pop(0)
                cSum += node.val
            
                if node.left:
                   queue.append(node.left)
                if node.right:
                   queue.append(node.right)
            
            if cSum > max_sum:
                max_sum = cSum
                result = level
            level += 1
        
        return result

# Driver code
if __name__ == '__main__':
    root1 = [1,7,0,7,-8,None,None]
    max_sum1 = Solution().maxLevelSum(root1)
    print("Maximum level sum from tree1:", max_sum1)