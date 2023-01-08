class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        u=moves.count('U')
        d=moves.count('D')
        l=moves.count('L')
        r=moves.count('R')
        u_d=u-d
        l_r=l-r
        
        
        return u_d==0 and l_r==0
