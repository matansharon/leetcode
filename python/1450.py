class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        res=0
        for i in range(0,len(startTime)):
            if startTime[i]<=queryTime and endTime[i]>=queryTime:
                res+=1
        return res
        
