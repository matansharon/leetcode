# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
# Example 4:

# Input: pattern = "abba", s = "dog dog dog dog"
# Output: false
 

# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lower-case English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.


class Solution(object):
    def wordPattern(self, pattern, st):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        s=st.split(' ')
        p=pattern
        if len(s)!=len(p):
            return False
        set_s=set()
        set_p=set()
        for i in s:
            set_s.add(i)
        for i in p:
            set_p.add(i)
        if len(set_s)!=len(set_p):
            return False
        dic={}
        
        for i in range(len(s)):
            if p[i] not in dic:
                dic[p[i]]=s[i]
        for i in range(len(p)):
            if dic[p[i]]!=s[i]:
                return False
        return True
        
        
            
        
        
        
