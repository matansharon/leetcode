class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occ=[]
        _set=set()
        for i in arr:
            _set.add(i)
        
        for i in _set:
            occ.append(arr.count(i))
        for i in occ:
            temp=occ.count(i)
            if temp!=1:
                return False
        return True
