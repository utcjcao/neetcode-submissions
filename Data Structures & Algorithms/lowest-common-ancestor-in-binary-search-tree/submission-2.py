# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        ma, mi = max(p.val, q.val), min(p.val, q.val)
        while True:
            if (mi <= cur.val and cur.val <= ma):
                break
            elif cur.val >= ma:
                cur = cur.left
            else:
                cur = cur.right
        return cur
            