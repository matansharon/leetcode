class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels='aeiou'
        res=''
        for i in s:
            if i not in vowels:
                res+=i
        return res
                
