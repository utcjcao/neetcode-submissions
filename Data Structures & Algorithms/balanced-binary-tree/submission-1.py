# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def h(self, root):
        if root is None: return 0
        return 1+max(self.h(root.left), self.h(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        if abs(self.h(root.left)-self.h(root.right))>1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
        