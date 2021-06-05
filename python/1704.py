class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        half=len(s)/2
        vowels ='aeiouAEIOU'
        a=s[:half]
        b=s[half:]
        tempa=0
        tempb=0
        for i in range(0,len(a)):
            if a[i] in vowels:
                tempa+=1
            if b[i] in vowels:
                tempb+=1
        return tempa==tempb
