# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy head node to simplify the construction of the result list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Loop while there are nodes to process in l1 or l2, or if there is a leftover carry
        while l1 or l2 or carry:
            # Get values from current nodes, or 0 if a list has reached its end
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum for the current position and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Create a new node with the calculated digit and move the pointer
            current.next = ListNode(digit)
            current = current.next
            
            # Advance to the next nodes in l1 and l2 if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy_head.next


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna