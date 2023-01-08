class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr=s.split(' ')
        res=''
        for i in arr:
            for j in range(len(i)-1,-1,-1):
                res+=i[j]
            res+=' '
        res=res[:-1]
        return res
