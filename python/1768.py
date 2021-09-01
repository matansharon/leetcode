# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d


class Solution(object):
    def mergeAlternately(self,word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res=''
        len1=len(word1)
        len2=len(word2)
        min_len=0
        largest_word=''
        if len1<len2:
            min_len=len1
            largest_word=word2
            
        else:
            min_len=len2
            largest_word=word1
        for i in range(0,min_len):
            res+=word1[i]
            res+=word2[i]
        res+=largest_word[min_len:]
       
        return res
