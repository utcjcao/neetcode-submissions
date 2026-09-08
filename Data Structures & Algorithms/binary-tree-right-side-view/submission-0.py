# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        finished = []
        q = []
        nq = []
        if root is not None:
            q.append(root)
        while len(q) != 0:
            for i in range(len(q)):
                if q[i].left is not None:
                    nq.append(q[i].left)
                if q[i].right is not None:
                    nq.append(q[i].right)
                if i == len(q)-1:
                    finished.append(q[i].val)
            q, nq = nq, []
        return finished


        