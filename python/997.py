# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
# Example 4:

# Input: n = 3, trust = [[1,2],[2,3]]
# Output: -1
# Example 5:

# Input: n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3
 

# Constraints:

# 1 <= n <= 1000
# 0 <= trust.length <= 104
# trust[i].length == 2
# All the pairs of trust are unique.
# ai != bi
# 1 <= ai, bi <= n


class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if len(trust)==0:
            if n==1:
                return 1
            else:
                return -1
        _set=set()
        for i in trust:
            _set.add(i[1])
        arr=[]
        for i in trust:
            arr.append(i[1])
        _max=0
        pos=-1
        for i in _set:
            temp=arr.count(i)
            if temp>_max:
                _max=temp
                pot=i
        if _max!=n-1:
            return -1
        for i in trust:
            if i[0]==pot:
                return -1
        return pot
