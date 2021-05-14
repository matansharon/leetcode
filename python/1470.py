class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x=nums[0:n]
        y=nums[n:]
        res=[]
        flag=True
        
        for i in range(0,n):
            res.append(x[i])
            res.append(y[i])
        return res
