# Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

# (Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

# Since the answer may be large, return the answer modulo 10^9 + 7.

 

# Example 1:

# Input: n = 5
# Output: 12
# Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
# Example 2:

# Input: n = 100
# Output: 682289015
 

# Constraints:

# 1 <= n <= 100


class Solution(object):
    def factorial(self, n):
            if n<=0:
                return 1
            return n*factorial(n-1)
    def isPrime(self, n):
        for i in range(2, n//2):
            if n%i == 0:
                return 0
        return 1
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
       
    
        
        np = 2 # for 2 & 3
        for i in range(5, n+1):
            if self.isPrime(i):
                np += 1
        return (self.factorial(np) * self.factorial(n-np))%(7+10**9) if n>2 else 1
        
        
    
