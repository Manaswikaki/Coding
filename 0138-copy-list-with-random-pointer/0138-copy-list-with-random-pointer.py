class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Interweave copied nodes with original nodes
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next, None)
            curr.next = new_node
            curr = new_node.next
            
        # Step 2: Assign random pointers for the copied nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        # Step 3: Separate the original and copied lists
        curr = head
        copy_head = head.next
        copy_curr = copy_head
        
        while curr:
            curr.next = copy_curr.next
            curr = curr.next
            if curr:
                copy_curr.next = curr.next
                copy_curr = copy_curr.next
                
        return copy_head


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna