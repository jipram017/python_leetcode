# Leetcode 834 - Sum of Distances in Tree
# Level: HARD
# O(N) time, O(N) space

from typing import List

class Solution:
    graph, count, answer = [], [], []
    num_nodes = 0
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        self.graph = [set() for _ in range(N)]
        for edge in edges:
            self.graph[edge[0]].add(edge[1])
            self.graph[edge[1]].add(edge[0])
            
        self.count = [1 for _ in range(N)]
        self.answer = [0 for _ in range(N)]
        self.num_nodes = N
        
        self.dfs1(0, -1)
        self.dfs2(0, -1)
        
        return self.answer
    
    def dfs1(self, node, parent):
        for child in self.graph[node]:
            if child != parent:
                self.dfs1(child, node)
                self.count[node] += self.count[child]
                self.answer[node] += self.answer[child] + self.count[child]
        
    def dfs2(self, node, parent):
        for child in self.graph[node]:
            if child != parent:
                self.answer[child] = self.answer[node] - self.count[child] + (self.num_nodes - self.count[child])
                self.dfs2(child, node)
            
# Driver code
if __name__ == '__main__':
    N = 6
    edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    sum_dist = Solution().sumOfDistancesInTree(N, edges)
    print("Sum of distances in tree1:", sum_dist)