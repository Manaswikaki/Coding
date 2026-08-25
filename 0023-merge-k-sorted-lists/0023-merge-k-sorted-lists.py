import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # Push the head of each non-empty list into the heap
        for i, l in enumerate(lists):
            if l:
                # Include index 'i' as a tie-breaker for unique comparison
                heapq.heappush(heap, (l.val, i, l))
        
        dummy = ListNode(0)
        curr = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            # If there is a next node, push it into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna