class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        alph='abcdefghij'
        first_w=''
        second_w=''
        target_w=''
        target_num=0
        for i in firstWord:
            first_w+=str(alph.find(i))
        for i in secondWord:
            second_w+=str(alph.find(i))
        for i in targetWord:
            target_w+=str(alph.find(i))
        return int(first_w)+int(second_w)==int(target_w)
            
