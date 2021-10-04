# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

 

# Example 1:

# Input: word = "USA"
# Output: true
# Example 2:

# Input: word = "FlaG"
# Output: false
 

# Constraints:

# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)==1:
            return True
        first=word[0].isupper()
        second=word[1].isupper()
        if first and second:
            for i in range(2,len(word)):
                if word[i].islower():
                    return False
        if first and not second:
            for i in range(2,len(word)):
                if word[i].isupper():
                    return False
        if not first:
            for i in range(1,len(word)):
                if word[i].isupper():
                    return False
        return True
        
