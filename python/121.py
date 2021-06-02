class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res=0
        for i in range(0,len(prices)-1):
            buy=prices[i]
            m=max(prices[i+1:])
            print prices[i+1:]
            if res<(m-buy):
                res=m-buy
        return res
