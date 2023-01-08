# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

# Example 1:


# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true
# Example 2:


# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false
 

# Constraints:

# 1 <= n <= 2000
# 0 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no self-loops or repeated edges.


def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
    if len(edges) != n - 1: return False
    
    # Create an adjacency list.
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)
    
    # We still need a seen set to prevent our code from infinite
    # looping if there *is* cycles (and on the trivial cycles!)
    seen = {0}
    stack = [0]
    
    while stack:
        node = stack.pop()
        for neighbour in adj_list[node]:
            if neighbour in seen:
                continue
            seen.add(neighbour)
            stack.append(neighbour)
    
    return len(seen) == n
