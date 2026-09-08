# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def maxs(m, root, count):
            if root is None:
                return 0 
            if root.val >= m:
                m = root.val
                count += 1
            count += maxs(m, root.left, 0) + maxs(m, root.right, 0)
            return count
        
        return maxs(-101, root, 0)
            