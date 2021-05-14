class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_of_pairs=0
        len1=len(nums)
        for i in range(0,len1):
            if i==len1-1:
                break
            for j in range(i+1,len1):
                if nums[i]==nums[j]:
                    num_of_pairs+=1
        return num_of_pairs
