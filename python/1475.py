class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(0,len(prices)):
            flag=True
            temp=prices[i]
            for j in range(i+1,len(prices)):
                if prices[j]<=temp:
                    res.append(temp-prices[j])
                    break
                if j==len(prices)-1:
                    res.append(temp)
        res.append(prices[-1])
        return res
                
