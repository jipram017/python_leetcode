# Leetcode 105 - Construct Binary Tree from Inorder and Preorder Traversal
# Level: MEDIUM
# O(N) time, O(N) space

from typing import List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def printInorder(self, root) -> List[int]:
        res = []
        if root:
            res = self.printInorder(root.left) 
            res.append(root.val)
            res = res + self.printInorder(root.right)
        return res
        
class Solution:
    pre_idx = 0
    in_order, pre_order = [], []
    map = defaultdict(int)
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        index = 0
        self.in_order, self.pre_order, self.pre_idx = inorder, preorder, 0
        
        for i in range(len(inorder)):
            self.map[inorder[i]] = index
            index += 1
        return self.buildTreeHelper(0, len(inorder))
    
    def buildTreeHelper(self, startIdx, endIdx):
        if startIdx == endIdx:
            return None
        rootNode = TreeNode(self.pre_order[self.pre_idx])
        rootIdx = self.map[self.pre_order[self.pre_idx]]
        self.pre_idx += 1
        
        rootNode.left = self.buildTreeHelper(startIdx, rootIdx)
        rootNode.right = self.buildTreeHelper(rootIdx + 1, endIdx)
        
        return rootNode
        
# Driver code
if __name__ == '__main__':
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]    
    binary_tree = Solution().buildTree(preorder, inorder)
    print(TreeNode().printInorder(binary_tree))