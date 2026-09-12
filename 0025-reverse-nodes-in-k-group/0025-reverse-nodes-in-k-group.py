# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Check if there are at least k nodes left in the list
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        
        # Step 2: If we found k nodes, reverse them
        if count == k:
            prev = None
            curr = head
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # Step 3: Recurse for the remaining nodes and connect the chunks
            if head:
                head.next = self.reverseKGroup(curr, k)
            
            # prev becomes the new head of this reversed k-group
            return prev
        
        # Step 4: If there are fewer than k nodes left, leave them as they are
        return head


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna