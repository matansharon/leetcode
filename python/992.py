class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd=[]
        even=[]
        res=[]
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        pos=0
        while True:
            if len(odd)==len(even)==0:
                
                break
            if pos%2==0:
                if len(even)>0:
                    res.append(even.pop(0))
                else:
                    while len(odd)>0:
                        res.append(odd.pop(0))
            else:
                if len(odd)>0:
                    res.append(odd.pop(0))
                else:
                     while len(even)>0:
                        res.append(even.pop(0))
            pos+=1
        return res
