# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

 

# Example 1:

# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:

# Input: s = "abcd", k = 2
# Output: "bacd"
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 104


class Solution(object):
    def reverse_sub_string(self,sub):
        res=''
        for i in reversed(sub):
            res+=i
        return res
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s)<k:
            return self.reverse_sub_string(s)
        res=''
        start=0
        end=start+k
        flag=True
        while end<len(s)+k:
            
            temp=s[start:end]
            if flag:
                temp=self.reverse_sub_string(temp)
            # print start,end,flag,s[start:end]
            res+=temp
            start=end
            end+=k
            flag=not(flag)
        return res
            
