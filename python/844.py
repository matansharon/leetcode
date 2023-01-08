# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

 

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:

# Input: s = "a##c", t = "#a#c"
# Output: true
# Explanation: Both s and t become "c".
# Example 4:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
 

# Constraints:

# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.


class Solution(object):
    def convrt_to_array(self,s):
        res=[]
        for i in s:
            res.append(i)
        for i in range(1,len(res)):
            if res[i]=='#':
                res[i]==''
                j=i
                while j>-1:
                    if res[j].isalpha():
                        res[j]=''
                        break
                    j-=1
        for i in range(0,len(res)):
            if res[i]=='#':
                res[i]=''
        return res
    def convert_arr_to_srting(self,arr):
        res=''
        for i in arr:
            res+=i
        return res
        
        
        
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=self.convrt_to_array(s)
        
        s=self.convert_arr_to_srting(s)
        t=self.convrt_to_array(t)
        t=self.convert_arr_to_srting(t)
        return s==t
        
                
