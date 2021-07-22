class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        res=''
        sentence=sentence.split(' ')
        a='a'
        pos=1
        for i in sentence:
            word=i
            if word[0] in 'aeiouAEIOU':
                word=word+'ma'+a*pos
            else:
                c=word[0]
                word=word[1:]
                word=word+c+'ma'+a*pos
            res+=word+' '
            pos+=1
        return res[:-1]
        
