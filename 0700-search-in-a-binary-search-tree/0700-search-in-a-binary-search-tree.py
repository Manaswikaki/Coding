# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        # Traverse the tree while the node exists and we haven't found the target value
        while root is not None and root.val != val:
            # If the target value is smaller, look in the left subtree
            if val < root.val:
                root = root.left
            # If the target value is larger, look in the right subtree
            else:
                root = root.right
                
        # Returns the node if found, or None if it doesn't exist
        return root


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna