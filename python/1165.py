# There is a special keyboard with all keys in a single row.

# Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25). Initially, your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is |i - j|.

# You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

 

# Example 1:

# Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
# Output: 4
# Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
# Total time = 2 + 1 + 1 = 4. 
# Example 2:

# Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
# Output: 73
    
    
class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        curr=0
        sum1=0
        for i in range(0,len(word)):
            next_char=keyboard.find(word[i])
            
            sum1+=abs(next_char-curr)
            curr=next_char
        return sum1
        
