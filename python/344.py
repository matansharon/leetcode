class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        for i in range((len(s)-1)/2,-1,-1):
            temp=s[i]
            s[i]=s[len(s)-1-i]
            s[len(s)-i-1]=temp
            print s
