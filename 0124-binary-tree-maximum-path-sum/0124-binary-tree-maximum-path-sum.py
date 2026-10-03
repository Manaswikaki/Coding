# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        # Initialize the global maximum sum with negative infinity
        self.max_sum = float('-inf')
        
        def get_max_gain(node):
            if not node:
                return 0
            
            # Recursively calculate the maximum gain from left and right subtrees.
            # If the gain is negative, ignore it by taking max(0, gain).
            left_gain = max(0, get_max_gain(node.left))
            right_gain = max(0, get_max_gain(node.right))
            
            # Price of a new path with the current node as the highest turning point
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum path sum found so far
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the maximum gain the node can contribute to its parent
            return node.val + max(left_gain, right_gain)
            
        get_max_gain(root)
        return self.max_sum


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna