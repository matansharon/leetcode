from random import random,choice,randint
import string

class Solution(object):
    def check_solution(self,sub_of_word):
        #split the sub_of_word into words by len_of_word
        words=[]
        for i in range(0,len(sub_of_word),self.len_of_word):
            words.append(sub_of_word[i:i+self.len_of_word])
        words.sort()
        print(self.words,words,self.words==words)   
        return (sorted(self.words)==sorted(words))
        
        
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res=[]
        self.words=sorted(words)
        self.len_of_word=len(words[0])
        self.len_of_words=len(words)*self.len_of_word
        for i in range(0,len(s)):
            sub=(s[i:i+self.len_of_words])
            if len(sub)!=self.len_of_words:
                break
            else:
                if self.check_solution(sub):
                    res.append(i)
        return res
            

if __name__ == '__main__':
    st=Solution()
    s="barfoothefoobarman"
    words=["foo","bar"]
    res=st.findSubstring(s,words)
    print(res)
     
    
    
    
    
    

# def random_string(length):
    
#     return ''.join(random.choice(string.ascii_lowercase) for i in range(length))
# def random_list(length):
    
#     res=[]
#     for i in range(length):
#         res.append(random_string(5))
#     return res
# def random_input():
#     res=''
#     for i in range(5):
#         res+=str.join('',random_string(randint(10)))
#         res+=str.join('',random_list(randint(5)))
#     return res

# print(random_input())
       