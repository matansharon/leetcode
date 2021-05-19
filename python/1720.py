class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        res=[]
        res.append(first)
        for i in range(0,len(encoded)):
            res.append(res[i]^encoded[i])
        return res
            
