# For two strings s and t, we say "t divides s" if and only if s = t + ... + t  (t concatenated with itself 1 or more times)

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
# Example 4:

# Input: str1 = "ABCDEF", str2 = "ABC"
# Output: ""
 

# Constraints:

# 1 <= str1.length <= 1000
# 1 <= str2.length <= 1000
# str1 and str2 consist of English uppercase letters.


m, n = len(str1), len(str2)
        
        for i in range(min(m, n), 0, -1):
            if n % i > 0 or m % i > 0: continue
                
            a, b = m // i, n // i
            test = str2[:i]
            if test * a == str1 and test * b == str2:
                return test
        
        return ''
