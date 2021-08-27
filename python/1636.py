# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

# Return the sorted array.

 

# Example 1:

# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
# Example 2:

# Input: nums = [2,3,1,3,2]
# Output: [1,3,3,2,2]
# Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
# Example 3:

# Input: nums = [-1,1,-6,4,5,-6,1,4,1]
# Output: [5,-1,4,4,-6,-6,1,1,1]



class Solution(object):
    def my_sort(self,arr):
        for i in range(0,len(arr)-1):
            if arr[i][0]==arr[i+1][0]:
                if arr[i][1]<arr[i+1][1]:
                    temp=arr[i]
                    arr[i]=arr[i+1]
                    arr[i+1]=temp
        return arr
    def convert_freq(self,arr):
        res=[]
        for i in arr:
            for j in range(0,i[0]):
                res.append(i[1])
        return res
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=[]
        _set=set()
        res=[]
        for i in nums:
            _set.add(i)
        for i in _set:
            arr.append([nums.count(i),i])
        
        arr.sort()
        arr=self.my_sort(arr)
        
       
        res=[]
        freq=arr[0][0]
        temp=[]
        
        print res
