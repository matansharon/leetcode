# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        node=head
        list1=[]
        count=0
        res=0
        while node:
            temp=pow(2,count)
            list1.append(temp)
            node=node.next
            count+=1
        
        node=head
        pos=len(list1)-1
        while node:
            if node.val==1:
                res+=list1[pos]
            pos-=1
            node=node.next
            
        return res
        
