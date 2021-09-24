# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

# Example 1:


# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: l1 = [], l2 = []
# Output: []
# Example 3:

# Input: l1 = [], l2 = [0]
# Output: [0]




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1=l1
        ptr2=l2
        arr=[]
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        while ptr1:
            arr.append(ptr1.val)
            ptr1=ptr1.next
        while ptr2:
            arr.append(ptr2.val)
            ptr2=ptr2.next
        arr.sort()
        head=ListNode(arr[0])
        ptr1=head
        for i in range(1,len(arr)):
            temp=ListNode(arr[i])
            ptr1.next=temp
            ptr1=ptr1.next
        return head
            
        
