# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        
        # Step 1: Determine if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If they meet, a cycle is detected
            if slow == fast:
                break
        else:
            # If fast reaches the end, there is no cycle
            return None
        
        # Step 2: Find the entry point of the cycle
        # Reset slow to head, leave fast at the meeting point
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna