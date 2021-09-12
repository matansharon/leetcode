# Write a function that reverses a string. The input string is given as an array of characters s.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]



class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        for i in range((len(s)-1)/2,-1,-1):
            temp=s[i]
            s[i]=s[len(s)-1-i]
            s[len(s)-i-1]=temp
            print s
