class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        
        if (coordinates[0] in 'aceg' and coordinates[1] in '1357') or (coordinates[0] in 'bdfh' and coordinates[1] in '2468'):
            return False
        
        return True
