# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge case: empty list, single node, or no rotation needed
        if not head or not head.next or k == 0:
            return head
        
        # 1. Compute the length of the list and find the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        # 2. Normalize k (handle k greater than length)
        k = k % length
        if k == 0:
            return head # No rotation needed after modulo
            
        # 3. Connect tail to head to form a circle
        tail.next = head
        
        # 4. Find the new tail: (length - k - 1) steps from head
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
            
        # 5. Break the circle and set the new head
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna