class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        res=[]
        
        # for i in range(0,len(nums)):
        #     res.append(0)
        # print(res)
        for i in range(0,len(nums)):    
            res.insert(index[i],nums[i])
        return res
