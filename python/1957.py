# A fancy string is a string where no three consecutive characters are equal.

# Given a string s, delete the minimum possible number of characters from s to make it fancy.

# Return the final string after the deletion. It can be shown that the answer will always be unique.

 

# Example 1:

# Input: s = "leeetcode"
# Output: "leetcode"
# Explanation:
# Remove an 'e' from the first group of 'e's to create "leetcode".
# No three consecutive characters are equal, so return "leetcode".
# Example 2:

# Input: s = "aaabaaaa"
# Output: "aabaa"
# Explanation:
# Remove an 'a' from the first group of 'a's to create "aabaaaa".
# Remove two 'a's from the second group of 'a's to create "aabaa".
# No three consecutive characters are equal, so return "aabaa".
# Example 3:

# Input: s = "aab"
# Output: "aab"
# Explanation: No three consecutive characters are equal, so return "aab".


class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        current, count, to_return = 0, 0, list()
        for i, char in enumerate(s):
            if char != current:
                current = char
                count = 1
                to_return.append(char)
            else:
                count += 1
                if count == 3:
                    count -= 1
                else:
                    to_return.append(char)
        return "".join(to_return)
#         arr=[]
#         for i in s:
#             arr.append(i)
#         # print arr
#         i=0
#         while i<len(arr)-2:
#             a=arr[i]
#             b=arr[i+1]
#             c=arr[i+2]
#             if a==b==c:
#                 # print temp
#                 arr.pop(i)
#             else:
#                 i+=1
#         res=''.join(arr)
        
#         return res
