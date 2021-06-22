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
