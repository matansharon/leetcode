class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        d_des=set()
        al=set()
        for i in paths:
            d_des.add(i[0])
            al.add(i[0])
            al.add(i[1])
        for i in al:
            if i not in d_des:
                return i
        return ''
            
