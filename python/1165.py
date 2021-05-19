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
        
