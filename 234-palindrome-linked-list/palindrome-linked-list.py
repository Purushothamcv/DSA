# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        x=[]
        
        while head:
            
            x.append(head.val)
            head=head.next
        y=x[::-1]
        if x==y:
            return True
        else:
            return False 
        