# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        p_left = p_right = 0
        while p_left < LEFT_BOUND and p_right < RIGHT_BOUND:
            # move both pointers or just the right pointer
            if s[p_left] == t[p_right]:
                p_left += 1
            p_right += 1

        return p_left == LEFT_BOUND
#         if s in t:
#             return True
#         res=0
#         arr=[]
#         for left in range(len(s)):
#             if s[left] in t:
#                 arr.append(t.index(s[left]))
#             for right in range(left,len(t)):
#                 if s[left]==t[right]:
#                     res+=1
#         print res
#         in_order=True
#         print arr
#         for i in range(len(arr)-1):
#             if arr[i+1]<=arr[i]:
#                 in_order=False
            
#         if res==len(s) and in_order:
#             return True
#         return False
