# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if list is empty or has only one node, it is already sorted
        if not head or not head.next:
            return head
        
        # Step 1: Split the list into two halves using slow and fast pointers
        prev = None
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        # Disconnect the first half from the second half
        prev.next = None
        
        # Step 2: Recursively sort each half
        left_side = self.sortList(head)
        right_side = self.sortList(slow)
        
        # Step 3: Merge the two sorted halves
        return self.merge(left_side, right_side)
        
    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        # Attach the remaining nodes of whichever list is not empty
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
            
        return dummy.next


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna