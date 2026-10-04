# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        # Helper function to compute the height along the leftmost path
        def get_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        left_h = get_height(root.left)
        right_h = get_height(root.right)
        
        if left_h == right_h:
            # The left subtree is a perfect binary tree of height left_h.
            # Number of nodes in left subtree + root = 2^left_h
            return (1 << left_h) + self.countNodes(root.right)
        else:
            # The right subtree is a perfect binary tree of height right_h (which is left_h - 1).
            # Number of nodes in right subtree + root = 2^right_h
            return (1 << right_h) + self.countNodes(root.left)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna