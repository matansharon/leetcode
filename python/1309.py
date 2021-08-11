# Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
# Return the string formed after mapping.

# It's guaranteed that a unique mapping will always exist.

 

# Example 1:

# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
# Example 2:

# Input: s = "1326#"
# Output: "acz"
# Example 3:

# Input: s = "25#"
# Output: "y"
# Example 4:

# Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
# Output: "abcdefghijklmnopqrstuvwxyz"



class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        low='abcdefghi'
        up='jklmnopqrstuvwxyz'
        res=''
        result=''
        pos=len(s)-1
        while pos>-1:
            if s[pos]=='#':
                temp_s=s[pos-2]+s[pos-1]
                temp_i=int(temp_s)
               
                res+=up[temp_i-10]
                
                pos-=3
            else:
                temp_i=int(s[pos])
                res+=low[temp_i-1]
                
                pos-=1
        for i in range(len(res)-1,-1,-1):
            result+=res[i]
        return result
