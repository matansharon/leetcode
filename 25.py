# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

#build some input test case
from random import randint
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def generate_list(self):
        head=ListNode(randint(0,100))
        curr=head
        for i in range(20):
            curr.next=ListNode(randint(0,100))
            curr=curr.next
        return head
    def print_list(self,head):
        curr=head
        while curr:
            print(curr.val,'->',end='')
            curr=curr.next
        print('|||')
    def convert_to_list(self,head):
        curr=head
        res=[]
        while curr:
            res.append(curr.val)
            curr=curr.next
        return res
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        self.print_list(head)
        if head.next==None:
            return head
        curr=head
        count=0
        while curr:
            count+=1
            curr=curr.next
        if count<k:
            return head
        curr=head
        prev=None
        next=None
        count=0
        while curr and count<k:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            count+=1
        if next:
            head.next=self.reverseKGroup(next,k)
        return prev

        
if __name__ == '__main__':
    s=Solution()
    #build some input test case
    head=s.generate_list()
    s.reverseKGroup(head,3)
      

        
    
    


   