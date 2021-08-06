# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

 

# Example 1:

# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]


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
