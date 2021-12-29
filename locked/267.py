# Given a string s, return all the palindromic permutations (without duplicates) of it.

# You may return the answer in any order. If s has no palindromic permutation, return an empty list.

 

# Example 1:

# Input: s = "aabb"
# Output: ["abba","baab"]
# Example 2:

# Input: s = "abc"
# Output: []
 

# Constraints:

# 1 <= s.length <= 16
# s consists of only lowercase English letters.


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        chars=Counter(s)
        
        if sum(v%2 for c,v in chars.items())>1: return []
        
        center=""
        letters=""
        for c,v in chars.items():
            if v%2:
                center=c
            letters+=c*(v//2)

        def permuteUnique(letters):
            ans = [""]
            for c in letters:
                new_ans = []
                for candidate in ans:
                    for i in range(len(candidate)+1):
                        new_ans.append(candidate[:i]+c+candidate[i:])
                        if i<len(candidate) and candidate[i]==c:
                            break              #handles duplication
                ans = new_ans
            print(ans)
            return ans
        
        return [x+center+x[::-1] for x in permuteUnique(letters)]
