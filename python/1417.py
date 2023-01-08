# Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

# You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

# Return the reformatted string or return an empty string if it is impossible to reformat the string.

 

# Example 1:

# Input: s = "a0b1c2"
# Output: "0a1b2c"
# Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
# Example 2:

# Input: s = "leetcode"
# Output: ""
# Explanation: "leetcode" has only characters so we cannot separate them by digits.
# Example 3:

# Input: s = "1229857369"
# Output: ""
# Explanation: "1229857369" has only digits so we cannot separate them by characters.
# Example 4:

# Input: s = "covid2019"
# Output: "c2o0v1i9d"
# Example 5:

# Input: s = "ab123"
# Output: "1a2b3"
#---------------------------------this solotion is good for 301/302 test cases--------------------------
class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
    
        if len(s)<2:
            return s
        digits=[]
        alpha=[]
        for i in s:
            if str.isalpha(str(i)):
                alpha.append(i)
            if str.isdigit(str(i)):
                digits.append(i)
        print digits
        print alpha
        if len(digits)==0 or len(alpha)==0:
            return ''
        if len(digits)== len(alpha):
            res=''
            for i in range(len(alpha)):
                res+=alpha[i]
                res+=digits[i]
            return res
        if len(digits)-len(alpha)==1:
            res=''
            for i in range(len(alpha)):
                res+=digits[i]
                res+=alpha[i]
            res+=digits[-1]
            return res
        if len(alpha)- len(digits)==1:
            res=''
            for i in range(len(digits)):
                res+=alpha[i]
                res+=digits[i]
            res+=alpha[-1]
            return res
