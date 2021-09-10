# A string is good if there are no repeated characters.

# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

# A substring is a contiguous sequence of characters in a string.

 

# Example 1:

# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
# The only good substring of length 3 is "xyz".
# Example 2:

# Input: s = "aababcabc"
# Output: 4
# Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
# The good substrings are "abc", "bca", "cab", and "abc".


class Solution(object):
    def check_for_good(self,sub):
        for i in range(len(sub)):
                if sub[i] in sub[i+1:]:
                    print False,sub
                    return False
        print True,sub
        return True
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        if len(s)<3:
            return 0
        if len(s)==3:
            if self.check_for_good(s):
                res+=1
            
        else:
            for i in range(0,len(s)-2):
                sub=s[i:i+3]
                if self.check_for_good(sub):
                    res+=1
        return res
        
