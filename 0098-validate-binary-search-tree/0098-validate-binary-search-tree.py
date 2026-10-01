# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            # An empty tree is a valid BST
            if not node:
                return True
            
            # The current node's value must be strictly within the low and high bounds
            if not (low < node.val < high):
                return False
            
            # Recursively check the left and right subtrees with updated bounds
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        
        return validate(root)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna