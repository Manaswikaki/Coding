# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
            
        def isMirror(t1: TreeNode | None, t2: TreeNode | None) -> bool:
            # If both nodes are null, they are symmetric
            if not t1 and not t2:
                return True
            # If only one node is null, they are not symmetric
            if not t1 or not t2:
                return False
            # Check if current values match and their subtrees are mirrored
            return (t1.val == t2.val) and \
                   isMirror(t1.left, t2.right) and \
                   isMirror(t1.right, t2.left)
                   
        return isMirror(root.left, root.right)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna