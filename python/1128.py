# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

# Example 1:

# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
# Example 2:

# Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# Output: 3
 

# Constraints:

# 1 <= dominoes.length <= 4 * 104
# dominoes[i].length == 2
# 1 <= dominoes[i][j] <= 9


class Solution(object):
    
            
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        dom=dominoes
        dic={}
        for i in dom:
            if (i[0],i[1]) in dic:
                dic[i[0],i[1]]+=1
            elif (i[1],i[0]) in dic:
                dic[i[1],i[0]]+=1
            else:
                dic[i[0],i[1]]=1
        res=0
        for i in dic:
            if dic[i]>1:
                res+=dic[i]*(dic[i]-1)/2
        return int(res)
        
