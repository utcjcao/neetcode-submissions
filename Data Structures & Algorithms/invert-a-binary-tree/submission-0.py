# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def switch(self, root):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.switch(root.left)
        self.switch(root.right)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.switch(root)
        return root