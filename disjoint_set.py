# DISJOINT SETS
# O(N) time, O(N) space

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    # A function to add an edge to a graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    # A utility function to find subset of element m
    def find_parent(self, parent, m):
        if parent[m] == -1:
            return m
        if parent[m] != -1:
            return self.find_parent(parent, parent[m])
    
    # A utility function to do union of two sets        
    def union_it(self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set
    
    # A utility function to check whether a graph contains cycle or not
    def isCyclic(self):
        parent = [-1]*(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union_it(parent, x, y)

# Driver code
if __name__ == '__main__':
    graph = Graph(4)
    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(0, 3)
    
    if graph.isCyclic():
        print("The graph contains cycle")
    else:
        print("The graph is free of cycle")
                