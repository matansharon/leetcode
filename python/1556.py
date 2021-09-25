# Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

# Example 1:

# Input: n = 987
# Output: "987"
# Example 2:

# Input: n = 1234
# Output: "1.234"
# Example 3:

# Input: n = 123456789
# Output: "123.456.789"
# Example 4:

# Input: n = 0
# Output: "0"


class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        s=str(n)
        res=''
        if len(s)<=3:
            return s
        s=list(s)
        pos=len(s)-1
        cnt=3
        while pos>-1:
            if cnt==0:
                res+='.'
                cnt=3
            res+=s[pos]
            cnt-=1
            pos-=1
        res2=''
        for i in reversed(res):
            res2+=i
        return res2
