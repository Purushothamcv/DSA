class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode or None
        """
        slow = fast = head

        # Step 1: Detect cycle using two pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Cycle detected, now find the entry point
                pointer = head
                while pointer != slow:
                    pointer = pointer.next
                    slow = slow.next
                return pointer  # Start of cycle

        return None  # No cycle
