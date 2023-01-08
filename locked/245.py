# Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

# Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list.

 

# Example 1:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
# Output: 1
# Example 2:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
# Output: 3
 

# Constraints:

# 1 <= wordsDict.length <= 105
# 1 <= wordsDict[i].length <= 10
# wordsDict[i] consists of lowercase English letters.
# word1 and word2 are in wordsDict.


class Solution:    
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        dis = math.inf
        w1, w2 = None, None
        for i, w in enumerate(wordsDict):
            if w == word1 and word1 == word2:
                if w2 is not None: dis = min(dis, i - w2)
                w1 = w2 = i                
            elif w == word1:
                if w2 is not None: dis = min(dis, i - w2)
                w1 = i
            elif w == word2:
                if w1 is not None: dis = min(dis, i - w1)
                w2 = i
        return dis  
