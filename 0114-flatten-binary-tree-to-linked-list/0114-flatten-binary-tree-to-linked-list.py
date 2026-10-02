# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        
        while curr:
            if curr.left:
                # Find the rightmost node in the left subtree
                rightmost = curr.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                # Rewire the rightmost node's right to current's right
                rightmost.right = curr.right
                
                # Move the left subtree to the right side
                curr.right = curr.left
                curr.left = None
            
            # Move to the next node on the right path
            curr = curr.right


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna