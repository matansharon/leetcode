class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        alpha='abcdefghijklmnopqrstuvwxyz'
        for i in alpha:
            pos=sentence.find(i)
            if pos==-1:
                return False
        return True
