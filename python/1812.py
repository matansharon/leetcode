# You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.



# Return true if the square is white, and false if the square is black.

# The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

 

# Example 1:

# Input: coordinates = "a1"
# Output: false
# Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
# Example 2:

# Input: coordinates = "h3"
# Output: true
# Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.
# Example 3:

# Input: coordinates = "c7"
# Output: false


class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        
        if (coordinates[0] in 'aceg' and coordinates[1] in '1357') or (coordinates[0] in 'bdfh' and coordinates[1] in '2468'):
            return False
        
        return True
