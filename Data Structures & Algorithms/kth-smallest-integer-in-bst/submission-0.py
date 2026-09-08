# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def travel(self, root, k):
        if root is not None:
            left_result = self.travel(root.left, k)
            if left_result is not None:
                return left_result
            self.counter += 1
            if (self.counter == k):
                return root.val
            right_result = self.travel(root.right, k)
            if right_result is not None:
                return right_result
        else:
            return None
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        return self.travel(root, k)
        