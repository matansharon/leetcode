# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        len1=0
        ptr=head
        while ptr:
            len1+=1
            ptr=ptr.next
        len1=len1/2
        ptr=head
        while len1>0:
            ptr=ptr.next
            len1-=1
        return ptr
