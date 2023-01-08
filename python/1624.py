# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 'a's.
# Example 2:

# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".
# Example 3:

# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.
# Example 4:

# Input: s = "cabbac"
# Output: 4
# Explanation: The optimal substring here is "abba". Other non-optimal substrings include "bb" and "".


class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        _set=set()
        res=''
        tempc=s[0]
        all_same=True
        for i in s:
            if i!=tempc:
                all_same=False
        if all_same:
            return 0
        for i in s:
            _set.add(i)
        for i in _set:
            first=s.index(i)
            last=s.rindex(i)
            if len(s[first+1:last])>len(res):
                res=s[first+1:last]
        if len(res)==0:
            return -1
        return len(res)
