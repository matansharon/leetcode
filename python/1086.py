class Solution(object):
    
    
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        s_items=sorted(items)
        
        id1=s_items[0][0]
        temp=[]
        res=[]
        for i in s_items:
            if i[0]==id1:
                temp.append(i[1])
            else:
                res.append([id1,sum(temp[-5:len(temp)])/5])
                id1=i[0]
                temp=temp[0:0]
                
                temp.append(i[1])
        
        res.append([id1,sum(temp[-5:len(temp)])/5])
        return res
