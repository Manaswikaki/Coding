# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def get_height(node):
            if not node:
                return 0
            
            # Recursively find the height of left and right subtrees
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            # The diameter at the current node is the sum of left and right heights
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return the height of the current subtree to the parent call
            return 1 + max(left_height, right_height)
        
        get_height(root)
        return self.max_diameter


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna