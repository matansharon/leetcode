class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_par=0
        close_par=0
        max_par=0
        for i in s:
            if i=="(":
                open_par+=1
            if i==")":
                close_par+=1
            temp_max=open_par-close_par
            if temp_max>max_par:
                max_par=temp_max
        return max_par
