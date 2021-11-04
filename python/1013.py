# Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

# Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

 

# Example 1:

# Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
# Example 2:

# Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false
# Example 3:

# Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

# Constraints:

# 3 <= arr.length <= 5 * 104
# -104 <= arr[i] <= 104


class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool    
        """
        m = sum(arr)
        if m%3 != 0:
            return False
        x = m//3
        z = 0
        l = []
        for p,q in enumerate(arr):
            z += q
            if z == x:
                l.append(p)
                z = 0
        if len(l) >= 2:
            for i in range(len(l)-1,-1,-1):
                if l[0]<l[i] and len(arr)-1!=l[i]:
                    return True
        else:
            return False
