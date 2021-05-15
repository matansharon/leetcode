class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res=[]
        
        
        for i in range(0,len(nums)):
            count=0
            for j in range(0,len(nums)):
                if i!=j and nums[i]>nums[j]:
                    count+=1
            res.append(count)
            
        return res
        
