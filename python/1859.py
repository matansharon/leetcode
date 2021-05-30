class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        list1=s.split(' ')
        res=''
        num_of_words=len(list1)+1
        
        
        for i in range(1,num_of_words):
            for w in list1:
                if str(i)in w:
                    res+=w[:-1]+' '
        return res[:-1]
