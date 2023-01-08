# Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.

# For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.
# Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same applies if there is no 1's.

 

# Example 1:

# Input: s = "1101"
# Output: true
# Explanation:
# The longest contiguous segment of 1s has length 2: "1101"
# The longest contiguous segment of 0s has length 1: "1101"
# The segment of 1s is longer, so return true.
# Example 2:

# Input: s = "111000"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 3: "111000"
# The longest contiguous segment of 0s has length 3: "111000"
# The segment of 1s is not longer, so return false.
# Example 3:

# Input: s = "110100010"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 2: "110100010"
# The longest contiguous segment of 0s has length 3: "110100010"
# The segment of 1s is not longer, so return false.


class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ones=1
        zeros=1
        max_ones=0
        max_zeros=0
        prev=s[0]
        for i in range(1,len(s)):
            
            if s[i]=='1'and prev=='1':
                ones+=1
            if s[i]=='0'and prev=='0':
                zeros+=1
            if s[i]=='1'and prev=='0':
                if ones>max_ones:
                    max_ones=ones
                    ones=1
            if s[i]=='0'and prev=='1':
                if zeros>max_zeros:
                    max_zeros=zeros
                    zeros=1
            perv=s[i]
        # print max_ones,max_zeros
                
        
