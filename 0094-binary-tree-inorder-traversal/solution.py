# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)      # 1. Visit left subtree
            res.append(node.val)    # 2. Visit node itself
            inorder(node.right)     # 3. Visit right subtree

        inorder(root)
        return res
        
