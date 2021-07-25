class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]
        first_row='qwertyuiopQWERTYUIOP'
        second_row='asdfghjklASDFGHJKL'
        third_row='zxcvbnmZXCVBNM'
        for word in words:
            flag=True
            temp_row=''
            if word[0] in first_row:
                temp_row=first_row
            elif word[0] in second_row:
                temp_row=second_row
            else:
                temp_row=third_row
            
            for c in word:
                if c not in temp_row:
                    flag=False
            if flag:
                res.append(word) 
            else:
                flag=True
        return res
        
