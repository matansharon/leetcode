# Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 

# Example 1:

# Input: s = "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"
# Example 2:

# Input: s = "aeiou"
# Output: ""


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
                
