class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        for i in target:
            pos=-1
            try:
                pos= arr.index(i)
            except:
                print 'not in array'
            arr.pop(pos)
            if pos==-1:
                return False
        return True
                
