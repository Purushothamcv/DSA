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
        i=0
        j=len(x)-1
        n=len(x)
        while i<j:
            if x[i]==x[j]:
                i+=1
                j-=1
            else:
                return False
        return True 

        # if x==y:
        #     return True
        # else:
        #     return False 
        