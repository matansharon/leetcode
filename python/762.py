# Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

# Recall that the number of set bits an integer has is the number of 1's present when written in binary.

# For example, 21 written in binary is 10101 which has 3 set bits.
 

# Example 1:

# Input: left = 6, right = 10
# Output: 4
# Explanation:
# 6 -> 110 (2 set bits, 2 is prime)
# 7 -> 111 (3 set bits, 3 is prime)
# 9 -> 1001 (2 set bits , 2 is prime)
# 10->1010 (2 set bits , 2 is prime)
# Example 2:

# Input: left = 10, right = 15
# Output: 5
# Explanation:
# 10 -> 1010 (2 set bits, 2 is prime)
# 11 -> 1011 (3 set bits, 3 is prime)
# 12 -> 1100 (2 set bits, 2 is prime)
# 13 -> 1101 (3 set bits, 3 is prime)
# 14 -> 1110 (3 set bits, 3 is prime)
# 15 -> 1111 (4 set bits, 4 is not prime)


class Solution(object):
    def is_prime(self,num):
        if num<8:
            if  num==2 or num==3 or num==5 or num==7:
                return True
            else:
                return False
        else:
            if num%2==0 or num%3==0 or num%5==0 or num%7==0:
                return False
            else:
                return True
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        res=0
        for i in range(left,right+1):
            
            
            c=bin(i).count('1')
            if self.is_prime(c):
                res+=1
        return res
        
