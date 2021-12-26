# Given a string s, return the length of the longest substring that contains at most two distinct characters.

 

# Example 1:

# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" which its length is 3.
# Example 2:

# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" which its length is 5.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of English letters.


from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        n = len(s)
        if n < 3:
            return n

        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position
        # in the sliding window
        hashmap = defaultdict()

        max_len = 2

        while right < n:
            # when the slidewindow contains less than 3 characters
            hashmap[s[right]] = right
            right += 1

            # slidewindow contains 3 characters
            if len(hashmap) == 3:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len
