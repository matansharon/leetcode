# We have two special characters:

# The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
# Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

 

# Example 1:

# Input: bits = [1,0,0]
# Output: true
# Explanation: The only way to decode it is two-bit character and one-bit character.
# So the last character is one-bit character.
# Example 2:

# Input: bits = [1,1,1,0]
# Output: false
# Explanation: The only way to decode it is two-bit character and two-bit character.
# So the last character is not one-bit character.
 

# Constraints:

# 1 <= bits.length <= 1000
# bits[i] is either 0 or 1.


class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits)==1:
            return True
        while len(bits)>3:
            temp=bits.pop(0)
            if temp==1:
                bits.pop(0)
        print bits
        if len(bits)==3:
            if bits[0]==1:
                return True
            else:
                if bits[1]==1:
                    return False
                return True
        if len(bits)==2:
            if bits[0]==1:
                return False
            return True
