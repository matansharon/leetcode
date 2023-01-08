# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false
# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res=[]
        for i in range(len(s)):
            res.append(s[:i+1])
        for i in res:
            len1=len(i)
            
            flag=True
            for j in range(0,len(s),len(i)):
                if i!= s[j:j+len1]:
                    flag=False
            if flag and len(s[j:j+len1])<len(s):
                return True
            
        return False
