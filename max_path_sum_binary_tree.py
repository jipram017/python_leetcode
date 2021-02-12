# Leetcode 124
# O(N) time, O(1) space

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return self.helper(root)[0]
    
    def helper(self, node):
        if not node:
            return float('-inf'), 0
        
        left_via, left_down = self.helper(node.left)
        right_via, right_down = self.helper(node.right)
        
        via = max(node.val + max(0, left_down) + max(0, right_down), left_via, right_via)
        down = node.val + max(0, left_down, right_down)
        
        return via, down