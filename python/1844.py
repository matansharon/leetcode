class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=''
        alphabet='abcdefghijklmnopqrstuvwxyz'
        for i in range(0,len(s)):
            if i%2==0:
                res+=s[i]
            if i%2==1:
                pos=alphabet.index(s[i-1])
                
                pos+=int(s[i])
                print(pos)
                res+=alphabet[pos]
        return res
