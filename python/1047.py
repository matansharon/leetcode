# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

# Example 1:

# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
# Example 2:

# Input: s = "azxxzy"
# Output: "ay"



class Solution(object):
    def remove(self,s,pos):
        return s[:pos]+s[pos+2:]
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        _s=s
        len1=len(s)
        i=0
        while i<len1-1:
            
            if _s[i]==_s[i+1]:
                _s=self.remove(_s,i)
                
                len1-=2
                i-=2
                if i<0:
                    i=0
            else:
                i+=1
        return _s
            
