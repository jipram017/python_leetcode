# Leetcode 106 - Construct Binary Tree from Inorder and Postorder Traversal
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
    map = defaultdict(int)
    in_order, post_order = [],[]
    post_idx = 0
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        index = 0
        self.in_order, self.post_order = inorder, postorder
        self.post_idx = len(postorder) - 1
        
        for i in range(len(inorder)):
            self.map[inorder[i]] = index
            index +=1
        return self.buildTreeHelper(0, len(inorder) - 1)
    
    def buildTreeHelper(self, startIdx, endIdx):
        if startIdx > endIdx:
            return None
        rootNode = TreeNode(self.post_order[self.post_idx])
        rootIdx = self.map[self.post_order[self.post_idx]]
        self.post_idx -= 1
        
        rootNode.right = self.buildTreeHelper(rootIdx + 1, endIdx)
        rootNode.left = self.buildTreeHelper(startIdx, rootIdx - 1)
        
        return rootNode
        
# Driver code
if __name__ == '__main__':
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]   
    binary_tree = Solution().buildTree(inorder, postorder)
    print(TreeNode().printInorder(binary_tree))