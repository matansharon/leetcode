# You are given a sorted unique integer array nums.

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
 

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# Example 2:

# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
# Example 3:

# Input: nums = []
# Output: []
# Example 4:

# Input: nums = [-1]
# Output: ["-1"]
# Example 5:

# Input: nums = [0]
# Output: ["0"]
 

# Constraints:

# 0 <= nums.length <= 20
# -231 <= nums[i] <= 231 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.


class Solution(object):
    def summaryRanges(self, arr):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(arr)
        j = 1
        li = []
        curr_str = ""
        
        #base case
        if n == 1 or n==0:
            if n != 0:
                li.append(str(arr[0]))
            return li
        
        pointer = arr[0]
        while j < n:
            if arr[j-1] + 1 == arr[j]:
                curr_str = str(pointer) + "->"+ str(arr[j])
                j += 1
                
            elif arr[j-1] + 1 != arr[j] and arr[j-1] == pointer:
                li.append(str(arr[j-1]))
                pointer = arr[j]
                j += 1
                
            else:
                li.append(str(curr_str))
                pointer = arr[j]
                j += 1
                
        if pointer == arr[-1] and j >= n:
            li.append(str(pointer))
        
        if curr_str not in li and curr_str != "":
            li.append(str(curr_str))
        return li
#         if len(nums)==0:
#             return []
#         if len(nums)==1:
#             return [str(nums[0])]
#         res=[]
#         first=nums[0]
#         last=-1
#         for i in range(1,len(nums)):
            
#             if nums[i]==nums[i-1]+1:
#                 last=nums[i]
#             else:
#                 if last>-1:
#                     res.append(str(first)+'->'+str(last))
#                 else:
#                     res.append(str(first))
                
#                 first=nums[i]
#                 last=-1
#         if last>-1:
#             res.append(str(first)+'->'+str(last))
#         else:
#             res.append(str(first))
#         return res
