# You are given a string text of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that text contains at least one word.

# Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the returned string should be the same length as text.

# Return the string after rearranging the spaces.

 

# Example 1:

# Input: text = "  this   is  a sentence "
# Output: "this   is   a   sentence"
# Explanation: There are a total of 9 spaces and 4 words. We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.
# Example 2:

# Input: text = " practice   makes   perfect"
# Output: "practice   makes   perfect "
# Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces plus 1 extra space. We place this extra space at the end of the string.
# Example 3:

# Input: text = "hello   world"
# Output: "hello   world"
# Example 4:

# Input: text = "  walks  udp package   into  bar a"
# Output: "walks  udp  package  into  bar  a "
# Example 5:

# Input: text = "a"
# Output: "a"
 

# Constraints:

# 1 <= text.length <= 100
# text consists of lowercase English letters and ' '.
# text contains at least one word.


class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        x = text.count(' ')
        n = [i for i in text.split(' ') if len(i) >= 1]
        if len(n) == 1:
            return n[0] + ' '*x
        spaces = x//(len(n)-1)
        extra = x%(len(n)-1)
        return (' '*spaces).join(n) + extra*' '
#         if len(text)==1:
#             return text
        
#         arr=text.split(' ')
#         words=[]
#         spaces=text.count(' ')
        
#         for i in arr:
#             if i!='':
#                 words.append(i)
            
#         s=1
#         res=''
        
#         if len(words)==1 :
#             return words[0]+' '*spaces
#         s=(spaces/(len(words)-1))
        
#         print s
#         for w in range(len(words)-1):
#             res+=words[w]+' '*s
#         res+=words[-1]
#         if spaces%(len(words)-1)==0:
#             return res
#         if len(words)-1<spaces:
#             res+=' '*(spaces-len(words))
#         res+=' '
#         return res
