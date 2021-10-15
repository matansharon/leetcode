# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex start to vertex end.

# Given edges and the integers n, start, and end, return true if there is a valid path from start to end, or false otherwise.

 

# Example 1:


# Input: n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2
# Example 2:


# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], start = 0, end = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.
 

# Constraints:

# 1 <= n <= 2 * 105
# 0 <= edges.length <= 2 * 105
# edges[i].length == 2
# 0 <= ui, vi <= n - 1
# ui != vi
# 0 <= start, end <= n - 1
# There are no duplicate edges.
# There are no self edges.


class Solution(object):
    def validPath(self, n, edges, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type start: int
        :type end: int
        :rtype: bool
        """
        if start == end:
            return True
        
		# Default is an empty list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        queue = [start]
		
		# Default is False
        visited = defaultdict(bool)
        visited[start] = True
        
        while len(queue) > 0:
            v = queue.pop(0)
            for adj in graph[v]:
                if adj == end:
                    return True
                
                elif not visited[adj]:
                    visited[adj] = True
                    queue.append(adj)
        
        return False
#         if len(edges)==0:
#             return True
#         arr=[set([edges[0][0],edges[0][1]])]
        
#         for e in edges:
#             flag=False
#             for i in arr:
#                 if e[0] in i or e[1] in i:
#                     i.add(e[0])
#                     i.add(e[1])
#                     flag=True
#             if flag==False:
#                 arr.append(set([e[0],e[1]]))
               
#         for i in arr:
#             if start in i and end in i:
#                 return True
#         return False
                
            
            
        
