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
