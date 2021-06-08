class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        s_num=str(num)
        
        s=s_num.replace('6','9',1)
        return int(s)
                
        
