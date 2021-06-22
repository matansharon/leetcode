class Solution(object):
    def convert_to_binary_array(self,num):
        n=num
        res=''
        while n>0:
            res+=str(n%2)
            n/=2
        
        return res
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res=0
        temp=self.convert_to_binary_array(x^y)
        print temp
        for i in temp:
            if i=='1':
                res+=1
        return res
        
