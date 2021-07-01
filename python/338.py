class Solution(object):
    def convert_to_binary_string(self,num):
        
        res=''
        
        while num>0:
            res+=str(num%2)
            num/=2
        return res.count('1')
        
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        for i in range(n+1):
            res.append(self.convert_to_binary_string(i))
        return res
        
