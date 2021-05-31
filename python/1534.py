class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        res=0
        for i in range(0,len(arr)-2):
            for j in range(i+1,len(arr)-1):
                for k in range(j+1,len(arr)):
                    A=abs(arr[i]-arr[j])
                    B=abs(arr[j]-arr[k])
                    C=abs(arr[i]-arr[k])
                    if A<=a and B<=b and C<=c:
                        res+=1
        return res
            
        
