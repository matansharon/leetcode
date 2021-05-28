class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        teams=n
        res=0
        while teams>1:
            res+=teams/2
            if teams%2==0:
                teams/=2
            else:
                teams=teams/2+1
        return res
