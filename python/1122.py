class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        temp=[]
        res=[]
        
        not_in_arr2=[]
        for i in arr1:
            if i not in arr2 and i not in not_in_arr2:
                not_in_arr2.append(i)
        not_in_arr2.sort()
        for i in arr2:
            try:
                temp.append([i,arr1.count(i)])
            except:
                continue
        for i in not_in_arr2:
            temp.append([i,arr1.count(i)])
        for i in temp:
            for j in range(i[1]):
                res.append(i[0])
        return res
