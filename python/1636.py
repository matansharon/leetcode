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
