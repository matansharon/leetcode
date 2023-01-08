class Solution(object):
    def divide_num(self,num):
        
        flag=True
        s_num=str(num)
        for i in s_num:
            if i!='0':
                temp=int(i)
                if num%temp!=0:
                    flag=False
        if '0' in s_num:
            flag=False
        return flag
        
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res=[]
        for i in range(left,right+1):
            
            if self.divide_num(i):
                res.append(i)
        return res
