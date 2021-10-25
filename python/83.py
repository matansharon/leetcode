# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def print_list(self,head):
        ptr=head
        while ptr:
            print ptr.val
            ptr=ptr.next
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        ptr=head
        arr=[]
        while ptr:
            if ptr.val not in arr:
                arr.append(ptr.val)
            ptr=ptr.next
        
        head=ListNode(arr.pop(0))
        ptr=head
        for i in arr:
            temp=ListNode(i)
            ptr.next=temp
            ptr=ptr.next
        return head
        
        
