# Given the head of a singly linked list, return true if it is a palindrome.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        ptr=head
        arr=[]
        while ptr:
            arr.append(ptr.val)
            ptr=ptr.next
        for i in range(0,len(arr)):
            n1=arr[i]
            n2=arr[len(arr)-1-i]
            if n1!=n2:
                return False
        return True
        
