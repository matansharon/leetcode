# A decimal number can be converted to its Hexspeak representation by first converting it to an uppercase hexadecimal string, then replacing all occurrences of the digit 0 with the letter O, and the digit 1 with the letter I.  Such a representation is valid if and only if it consists only of the letters in the set {"A", "B", "C", "D", "E", "F", "I", "O"}.

# Given a string num representing a decimal integer N, return the Hexspeak representation of N if it is valid, otherwise return "ERROR".

 

# Example 1:

# Input: num = "257"
# Output: "IOI"
# Explanation:  257 is 101 in hexadecimal.
# Example 2:

# Input: num = "3"
# Output: "ERROR"


class Solution(object):
    def toHexspeak(self, num):
        """
        :type num: str
        :rtype: str
        """
        num=int(num)
        h=hex(num)
        h=h[2:]
        print h
        h2=''
        for i in h:
            if i.isalpha():
                h2+=str.upper(i)
            elif i=='1':
                h2+='I'
            elif i=='0':
                h2+='O'
            elif i.isdigit():
                return 'ERROR'
            
        return h2
