class RecentCounter(object):

    def __init__(self):
        self.range=[-3000,0]
        self.calls=[]
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        res=0
        self.range[0]=-3000+t
        self.range[1]=t
        self.calls.append(t)
        
        for i in self.calls:
            if i>=self.range[0]and i<=self.range[1]:
                res+=1
        return res
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
