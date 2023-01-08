# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr=[]
        vowels='aeiouAEIOU'
        
        for i in s:
            if i in vowels:
                arr.append(i)
        
        ptr=len(arr)-1
        for i in range(0,len(s)):
            if s[i] in vowels:
                s=s[:i]+arr[ptr]+s[i+1:]
                ptr-=1
        return s
