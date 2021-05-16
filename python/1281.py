class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        list_of_dig=[]
        Product=1
        Sum=0
        res=0
        while n>0:
            temp=n%10
            # list_of_dig.append(temp)
            Product*=temp
            Sum+=temp
            n/=10
        return Product-Sum
