class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        list1=s.split(' ')
        res=''
        for i in range(0,k):
            if i<k-1:
                res+=list1[i]+' '
            else:
                res+=list1[i]
        return res
