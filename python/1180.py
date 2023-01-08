# Given a string s, return the number of substrings that have only one distinct letter.

 

# Example 1:

# Input: s = "aaaba"
# Output: 8
# Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
# "aaa" occurs 1 time.
# "aa" occurs 2 times.
# "a" occurs 4 times.
# "b" occurs 1 time.
# So the answer is 1 + 2 + 4 + 1 = 8.
# Example 2:

# Input: s = "aaaaaaaaaa"
# Output: 55

class Solution(object):
    def my_fac(self,val):
        res=0
        for i in range(0,val+1):
            res+=1
        return res

    def countLetters(self, s):
        """
        :type s: str
        :rtype: int
        """
        row=1
        total=1
        for i in range(0,len(s)-1):
            if s[i]==s[i+1]:
                row+=1
            else:
                row=1
            total+=row
        
        return total
        
