# Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

# Example 1:

# Input: num = 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
# Example 2:

# Input: num = 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
class Solution(object):
    def convert_to_binary(self,num):
        res=''
        temp=bin(num)
        pos=temp.index('b')+1
        res=temp[pos:]
        return res
    def flip(self,num):
        res=''
        for i in num:
            if i=='1':
                res+='0'
            else:
                res+='1'
        return res
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp=self.convert_to_binary(num)
        temp=self.flip(temp)
        
        return int(temp,2)
