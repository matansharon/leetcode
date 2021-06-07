class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1=sorted(nums)
        res=0
        print(nums1)
        for i in range(0,len(nums1)-1):
            if nums1[i+1]==nums1[i]:
                print(nums1)
                nums1[i+1]+=1
                print(nums1)
                res+=1
            elif nums1[i+1]>nums1[i]:
                
                while nums1[i+1]-nums1[i]>1:
                    nums1[i]+=1
                    print(nums1)
                    res+=1
            else:
                print("else")
                while nums1[i]-nums1[i+1]>1:
                    nums1[i+1]+=1
                    print(nums1)
                    res+=1
        print(nums1)
        return res
                
