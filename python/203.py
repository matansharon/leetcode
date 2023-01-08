# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

# Example 1:


# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:

# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []
 

# Constraints:

# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object): 
    def print_list(self,head):
        ptr=head
        while ptr:
            print ptr.val,'->',
            ptr=ptr.next
        print '|||'
  
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head==None:
            return None
        
        curr=head   
        arr=[]
        while curr:
            arr.append(curr.val)
            curr=curr.next
        if arr.count(val)==len(arr):
            return None
        i=0
        while i<len(arr):
            if arr[i]==val:
                arr.pop(i)
            else:
                i+=1
        res=ListNode(arr[0])
        curr=res
        for i in range(1,len(arr)):
            temp=ListNode(arr[i])
            curr.next=temp
            curr=curr.next
        
        
        return res
