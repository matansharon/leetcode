class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        l=[0]*100
        for i in range(lowLimit,highLimit+1):
            pos=0
            num=i
            while num>0:
                pos+=num%10
                num/=10
            l[pos]+=1
        return max(l)
