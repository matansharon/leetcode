class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res=[] 
        res.append(0)
        curr=0
        max_al=0
        for i in range(0,len(gain)):
            curr+=gain[i]
            if curr>max_al:
                max_al=curr
        return max_al
            
