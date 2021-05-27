class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res=0
        max_len=len(arr)+1
        for length in range(1,max_len,2):
            i=0
            while i+length<max_len:
                temp=arr[i:i+length]
                for q in temp:
                    res+=q
                i+=1
        return res
