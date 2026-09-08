# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isEqual(self, root, subRoot):
        if not root and not subRoot: return True
        if root and subRoot and root.val == subRoot.val:
            return self.isEqual(root.right, subRoot.right) and self.isEqual(root.left, subRoot.left)
        return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return not subRoot
        if root and subRoot and self.isEqual(root, subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)