class Solution(object):
    def maxNumberOfApples(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        total=0
        res=0
        while len(arr)>0 and total<5000:
            temp=min(arr)
            pos=arr.index(temp)
            if total+temp<5000:
                total+=temp
                res+=1
                arr.pop(pos)
            else:
                break
            
        return res
