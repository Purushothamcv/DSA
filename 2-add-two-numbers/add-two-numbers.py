# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
    #     class ListNode:
    # def __init__(self, val=0, next=None):
    #     self.val = val
    #     self.next = next

# def addTwoNumbers(l1, l2):
        dummy = ListNode(0)  # Dummy node to simplify list construction
        current = dummy
        carry = 0  # Store carry-over value

        while l1 or l2 or carry:
            sum_val = carry  # Start with carry from previous operation

            if l1:
                sum_val += l1.val  # Add value from first list
                l1 = l1.next  # Move to next node

            if l2:
                sum_val += l2.val  # Add value from second list
                l2 = l2.next  # Move to next node

            carry = sum_val // 10  # Compute carry for next digit
            current.next = ListNode(sum_val % 10)  # Store last digit in new node
            current = current.next  # Move to next node

        return dummy.next 

        
            

        