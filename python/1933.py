# A value-equal string is a string where all characters are the same.

# For example, "1111" and "33" are value-equal strings.
# In contrast, "123" is not a value-equal string.
# Given a digit string s, decompose the string into some number of consecutive value-equal substrings where exactly one substring has a length of 2 and the remaining substrings have a length of 3.

# Return true if you can decompose s according to the above rules. Otherwise, return false.

# A substring is a contiguous sequence of characters in a string.

 

# Example 1:

# Input: s = "000111000"
# Output: false
# Explanation: s cannot be decomposed according to the rules because ["000", "111", "000"] does not have a substring of length 2.
# Example 2:

# Input: s = "00011111222"
# Output: true
# Explanation: s can be decomposed into ["000", "111", "11", "222"].
# Example 3:

# Input: s = "011100022233"
# Output: false
# Explanation: s cannot be decomposed according to the rules because of the first '0'.



class Solution(object):
    
    def isDecomposable(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pos=0
        last=0
        res=[]
        while pos<len(s)-1:
            if s[pos+1]!=s[pos]:
                res.append(s[last:pos+1])
                pos+=1
                last=pos
            pos+=1
        res.append(s[last:])
        number_of_len_2=0
        print res
        temp=[]
        for i in res:
            if len(i)%3==0:
                temp.append(0)
            elif (len(i)-2)%3==0:
                temp.append(2)
                temp.append(0)
            else:
                temp.append(len(i))
        
        try:
            temp.pop(temp.index(2))
        except:
            return False
        
        for i in temp:
            if i!=0:
                return False
        return True
                 
        
        
            
        
