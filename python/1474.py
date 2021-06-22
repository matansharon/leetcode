# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def convert_to_linked_list(self,arr):
        head=ListNode(arr[0])
        ptr=head
        for i in range(1,len(arr)):
            if arr[i]!=-1:
                node=ListNode(arr[i])
                ptr.next=node
                ptr=ptr.next
        self.print_list(head)
        return head
    def convert_to_array(self,head):
        ptr=head
        res=[]
        while ptr:
            res.append(ptr.val)
            ptr=ptr.next
        return res
    def print_list(self,head):
        ptr=head
        while ptr:
            print ptr.val,'->',
            ptr=ptr.next
        print '|||'
    def deleteNodes(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        arr=self.convert_to_array(head)
        keep=0
        _del=0
        for i in range(0,len(arr)):
            if keep<m:
                keep+=1
                continue
            if keep==m and _del<n:
                arr[i]=-1
                _del+=1
            if keep==m and _del==n:
                keep=0
                _del=0
        
        return self.convert_to_linked_list(arr)
        
               
