class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for i in nums:
            if dic.get(i):
                dic[i]+=1
            else:
                dic[i]=1
        
        for i in dic:
            if dic[i]==1:
                return i
