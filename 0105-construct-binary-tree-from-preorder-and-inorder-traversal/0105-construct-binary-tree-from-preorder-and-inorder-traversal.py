# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Hash map to find the index of any root value in O(1) time
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Pointer to keep track of the current element in preorder traversal
        self.pre_idx = 0
        
        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            # If there are no elements to construct the subtree
            if left > right:
                return None
            
            # Select the preorder_index element as the root and increment it
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            
            # Root splits inorder list into left and right subtrees
            index = inorder_index_map[root_val]
            
            # Build left and right subtrees
            # Crucial: Build the left subtree first because preorder elements are ordered sequentially
            root.left = array_to_tree(left, index - 1)
            root.right = array_to_tree(index + 1, right)
            
            return root
            
        return array_to_tree(0, len(inorder) - 1)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna