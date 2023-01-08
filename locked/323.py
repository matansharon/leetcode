# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

 

# Example 1:


# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2
# Example 2:


# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1
 

# Constraints:

# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.


class Solution:
    def traversal(self, g, visited, v):
        visited.add(v)
        
        for neigb in g[v]:
            if neigb not in visited:
                self.traversal(g, visited, neigb)
                
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0
        
        g = collections.defaultdict(list)
        visited = set()
        
        for (e1,e2) in edges:
            g[e1].append(e2)
            g[e2].append(e1)
        
        res = 0
        for v in range(n):
            if v not in visited:
                res += 1
                self.traversal(g, visited, v)
        
        return res
