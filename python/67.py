# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

class Solution(object):
    def convert_to_dec(self,num):
        res=0
        p=0
        for i in range(len(num)-1,-1,-1):
            
            if num[i]=='1':
                
                res+=pow(2,p)
            p+=1
        return res
    def convet_to_binary(self,dec):
        temp=''
        res=''
        while dec>0:
            r=dec%2
            temp+=(str(r))
            dec/=2
        for i in range(len(temp)-1,-1,-1):
            res+=temp[i]
        return res
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a=='0' and b=='0':
            return '0'
        n1=self.convert_to_dec(a)
         
        n2=self.convert_to_dec(b)
        
        sum_=n1+n2
        return self.convet_to_binary(sum_)
        
        
        
