# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr=head
        arr=[]
        if head==None:
            return None
        while ptr:
            arr.append(ptr.val)
            ptr=ptr.next
        res=ListNode(arr[-1])
        ptr=res
        arr.pop()
        while len(arr)>0:
            temp=ListNode(arr.pop())
            ptr.next=temp
            ptr=ptr.next
        return res
        
