# Definition for singly-linked list.
#
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Add digits and carry
            total = v1 + v2 + carry
            carry = total // 10
            digit = total % 10

            # Create new node
            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
