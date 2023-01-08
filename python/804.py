class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet='abcdefghijklmnopqrstuvwxyz'
        end=[]
        end2=set()
        res=0
        morse=[".-","-...","-.-.","-..",".","..-.",
               "--.","....","..",".---","-.-",".-..",
               "--","-.","---",".--.","--.-",".-.",
               "...","-","..-","...-",".--","-..-",
               "-.--","--.."]
        for w in words:
            temp_morse=''
            for c in w:
                pos=alphabet.index(c)
                temp_morse+=morse[pos]
            end.append(temp_morse)
        
        for i in end:
            end2.add(i)
        
        
        return len(end2)
                
