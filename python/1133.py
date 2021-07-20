class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _set=set()
        for i in nums:
            _set.add(i)
        _set=sorted(_set,reverse=True)
        for i in _set:
            if nums.count(i)==1:
                return i
        return -1
