# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 

# Example 1:


# Input: path = "NES"
# Output: false 
# Explanation: Notice that the path doesn't cross any point more than once.
# Example 2:


# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.



class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        visited = []; dirs = {"N": [-1, 0], "S": [1, 0], "W": [0, -1], "E": [0, 1]}
        cur = [0, 0]; visited.append(cur)
        
        for d in path:
            r, c = dirs[d]; cur = [cur[0]+r, cur[1]+c]
            if cur in visited:
                return True
            visited.append(cur)
    
        return False
