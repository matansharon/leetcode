# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them.

 

# Example 1:

# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.
# Example 2:

# Input: x = 3, y = 1
# Output: 1


class Solution(object):
    def convert_to_binary_array(self,num):
        n=num
        res=''
        while n>0:
            res+=str(n%2)
            n/=2
        
        return res
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res=0
        temp=self.convert_to_binary_array(x^y)
        print temp
        for i in temp:
            if i=='1':
                res+=1
        return res
        
        
