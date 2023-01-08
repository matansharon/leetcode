# Given an array words of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

# You may return the answer in any order.

 

# Example 1:

# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: ["cool","lock","cook"]
# Output: ["c","o"]

class Solution(object):
    def char_in_all_words(self,char,words):
        for word in words:
            if char not in word:
                return False
        return True
    def pop_char_from_all_words(self,char,words):
        temp_words=[]
        for word in words:
            if char in word:
                
                pos=word.index(char)
                temp_words.append(word[:pos]+word[pos+1:])
        return temp_words
                
                
        
                
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]
        temp_arr=words
        pos=0
        while pos<len(temp_arr[0]):
            char= temp_arr[0][pos]
            if self.char_in_all_words(char,temp_arr):
                res.append(char)
                temp_arr=self.pop_char_from_all_words(char,temp_arr)
                
            else:
                pos+=1
        return res
