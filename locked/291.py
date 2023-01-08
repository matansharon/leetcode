# Given a pattern and a string s, return true if s matches the pattern.

# A string s matches a pattern if there is some bijective mapping of single characters to strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.

 

# Example 1:

# Input: pattern = "abab", s = "redblueredblue"
# Output: true
# Explanation: One possible mapping is as follows:
# 'a' -> "red"
# 'b' -> "blue"
# Example 2:

# Input: pattern = "aaaa", s = "asdasdasdasd"
# Output: true
# Explanation: One possible mapping is as follows:
# 'a' -> "asd"
# Example 3:

# Input: pattern = "aabb", s = "xyzabcxzyabc"
# Output: false
 

# Constraints:

# 1 <= pattern.length, s.length <= 20
# pattern and s consist of only lowercase English letters.


class Solution:
    # algorithm: combination and early stop
    # step1: run combination and check the result and bijection is valid or not
    # time complexity: O(S^P)  I think it just a upper bound, because of early stop
    # space complexity: O(P)
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def combination(start, endS, step, endP, pToS={}, sToP={}):
            if step==endP:
                return start==endS
            if start==endS and step!=endP:
                return False
            p = pattern[step]
            if p in pToS:
                end_ = start+len(pToS[p])
                if end_<=endS and pToS[p]==s[start:end_]:
                    return combination(end_, endS, step+1, endP, pToS, sToP)
                else:
                    return False
            for i in range(start, endS):
                if s[start:i+1] in sToP:
                    continue
                pToS[p] = s[start:i+1]
                sToP[s[start:i+1]] = p
                if combination(i+1, endS, step+1, endP, pToS, sToP):
                    return True
                del pToS[p]
                del sToP[s[start:i+1]]
            return False
        return combination(0, len(s), 0, len(pattern))
