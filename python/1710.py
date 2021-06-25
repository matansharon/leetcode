class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        arr=[]
        num_of_boxes=0
        res=0
        BT=boxTypes
        TS=truckSize
        for i in BT:
            for j in range(0,i[0]):
                arr.append(i[1])
        arr.sort(reverse=True)
        
        for i in arr:
            if num_of_boxes<TS:
                res+=i
                num_of_boxes+=1
        return res
            
            
            
        
