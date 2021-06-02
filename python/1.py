class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res={}
        for i in range(0,len(nums)):
            res[nums[i]]=i
        print res
        for i in nums:
            temp=target-i
            if res.get(temp)!=None:
                n1=res[i]
                n2=res[temp]
                
                if n1!=n2:
                    return [n1,n2]
        return "match didnt found"
