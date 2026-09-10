# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle empty or single-node lists
        if not head:
            return None
        
        odd = head
        even = head.next
        evenHead = even  # Keep track of the starting even node to connect later
        
        # Traverse the list until we reach the end of either list
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        # Connect the end of the odd list to the beginning of the even list
        odd.next = evenHead
        
        return head


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna