import random
class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        ch1='a'
        ch2='b'
        res=''
        if n%2==1:
            return ('a')*n
        return ch1*(n-1)+('b')
        
        
