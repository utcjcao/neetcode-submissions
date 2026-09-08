# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def greater(root, prev):
            if root is None:
                return True
            if root.val <= prev:
                return False
            a = greater(root.right, root.val) and greater(root.left, prev)
            b = less(root.left, root.val)
            return a and b
        def less(root, prev):
            if root is None:
                return True
            if root.val >= prev:
                return False
            a = less(root.right, prev) and less(root.left, root.val)
            b = greater(root.right, root.val)
            return a and b
        
        if root is None:
            return True
        return greater(root.right, root.val) and less(root.left, root.val)
        