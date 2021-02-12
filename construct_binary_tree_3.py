# Leetcode 889 - Construct Binary Tree from Preorder and Postorder Traversal
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
    pre_idx = 0
    pre_order,post_order = [],[]
    
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        index = 0
        self.pre_order, self.post_order = pre, post 
        self.pre_idx = 0
        
        for i in range(len(post)):
            self.map[post[i]] = index
            index += 1
        return self.buildTreeHelper(0, len(pre) - 1)
    
    def buildTreeHelper(self, startIdx, endIdx):
        if startIdx > endIdx:
            return None
        rootNode = TreeNode(self.pre_order[self.pre_idx])
        
        self.pre_idx += 1
        if self.pre_idx == len(self.pre_order):
            return rootNode
        
        rootIdx = self.map[self.pre_order[self.pre_idx]]
        if startIdx < endIdx:
            rootNode.left = self.buildTreeHelper(startIdx, rootIdx)
            rootNode.right = self.buildTreeHelper(rootIdx + 1, endIdx - 1)
            
        return rootNode
    
# Driver code
if __name__ == '__main__':
    pre = [1,2,4,5,3,6,7]
    post = [4,5,2,6,7,3,1]
    binary_tree = Solution().constructFromPrePost(pre, post)
    print(TreeNode().printInorder(binary_tree))
        